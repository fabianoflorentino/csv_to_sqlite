"""
This program import a csv file to a sqlite database.
"""
# -*- coding: utf-8 -*-
import csv
import sqlite3
import sys


class DataBase:
    """Database class"""

    def __init__(self):
        self.conn = None
        self.cursor = None

    def create_database(self, db_name):
        """
        This function creates a database.
        """
        try:
            self.conn = sqlite3.connect(db_name)
        except sqlite3.Error as error:
            print(error)

    def create_table(self, db_name, sql_file):
        """
        This function creates a table in the database.
        """
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

            with open(sql_file, encoding='utf-8', mode='r') as sql_read:
                self.cursor.executescript(sql_read.read())

            self.conn.commit()
            self.conn.close()

        except sqlite3.Error as error:
            print(error)
            sys.exit(1)
        except AttributeError as error:
            print(error)
            sys.exit(1)

    def import_from_csv(self, csv_file, sql_file, db_name):
        """
        This function imports data from a csv file to a database.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        csv.register_dialect('csv_dialect', delimiter=';',
                             quoting=csv.QUOTE_ALL)
        with open(csv_file, encoding='utf-8', mode='r') as csv_read:
            csv_read = csv.reader(csv_read, dialect='csv_dialect')

            with open(sql_file, encoding='utf-8', mode='r') as sql_read:
                sql_read = sql_read.read()
                self.cursor.executemany(sql_read, csv_read)

        self.conn.commit()
        self.conn.close()

    def select_data(self, sql_file, db_name):
        """
        This function selects data from a database.
        """
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

            with open(sql_file, encoding='utf-8', mode='r') as sql_read:
                sql_read = sql_read.read()
                self.cursor.execute(sql_read)
                data_selet = self.cursor.fetchall()

            return print(str(data_selet).replace('),', '),\n'))
        except BrokenPipeError:
            sys.exit(1)


def help_me():
    """This function prints the help message"""
    help_msg = """
Description: This script imports a csv file into a sqlite database.

Usage: python3 main.py [OPTIONS] [ARGMENTS(1)] [FILE] [ARGUMENTS(2)] [FILE] [ARGUMENTS(3)]

Ex: python3 main.py -h or --help
    python3 main.py -c or --create_database [DATABASE_NAME]
    python3 main.py -d or --database [DATABASE_NAME] -f or --sql_file [SQL_FILE]
    python3 main.py -csv or --import_csv [CSV_FILE] -ts or --table_from_sql [TABLE_NAME] -d or --database [DATABASE_NAME]

Options:
    -h, --help                  Show this help message and exit
    -c, --create_database       Create a database
    
    -d, --database              Database options
        Options on -d or --database:
        -f, --sql_file          Create a table in the database
    
    -csv, --import_csv          Import data from csv file to database
        Options on -csv or --import_csv:
        -ts, --table_from_sql   Table name to import data
        -d, --database          Database name to import data
"""

    return print(help_msg)


def main():
    """
    This function has options and arguments to run the program
    """
    try:
        if sys.argv[1] in ('-h', '--help'):
            return help_me()

        if sys.argv[1] in ('-c', '--create_database'):
            create_database = DataBase()
            create_database.create_database(sys.argv[2])
            return print("Database created successfully")

        if sys.argv[1] in ('-d', '--database'):
            if sys.argv[3] in ('-f', '--sql_file'):
                create_table = DataBase()
                create_table.create_table(sys.argv[2], sys.argv[4])
                return print("Table created successfully")

        if sys.argv[1] in ('-csv', '--import_csv'):
            if sys.argv[3] in ('-ts', '--table_from_sql'):
                if sys.argv[5] in ('-d', '--database'):
                    csv_file = DataBase()
                    csv_file.import_from_csv(
                        sys.argv[2], sys.argv[4], sys.argv[6])
                    return print("Data imported successfully")

        if sys.argv[1] in ('-s', '--select_data'):
            if sys.argv[3] in ('-d', '--database'):
                select_data = DataBase()
                return select_data.select_data(sys.argv[2], sys.argv[4])

    except IndexError as error:
        print(error)
        sys.exit(1)
    except FileNotFoundError as error:
        print(error)
        sys.exit(1)

    return help_me()


if __name__ == "__main__":
    main()
