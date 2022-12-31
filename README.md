# CSV to SQLITE DATABASE

This is a simple program to convert a CSV file to a SQLITE database.

## **Supported Operating Systems**

All non-EOL versions below are supported.

* Windows
* Linux
* macOS

## **Dependencies**

* Python 3.10 or higher

## **Parameters**

| Parameter | Version Add | Type | Required | Description |
| :--- | :---: | :---: | :---: | :--- |
| `-h, --help` | 1.0.0 | Option | No | Show this help message and exit |
| `-c, --create_database` | 1.0.0 | Option | Yes | Create a database |
| `-d, --database` | 1.0.0 | Option | Yes | Database options |
| `-f, --sql_file` | 1.0.0 | Option | Yes | Create a table in the database |
| `-csv, --import_csv` | 1.0.0 | Option | Yes | Import data from csv file to database |
| `-ts, --table_from_sql` | 1.0.0 | Option | Yes | Table name to import data |
| `-d, --database` | 1.0.0 | Option | Yes | Database name to import data |

<br>

## **Usage**

```txt
python3 main.py [OPTIONS] [ARGMENTS(1)] [FILE] [ARGUMENTS(2)] [FILE] [ARGUMENTS(3)]
```

### **Example**

OBS: Tested on Linux environment.

```bash
python3 main.py -h or --help
python3 main.py -c or --create_database [DATABASE_NAME]
python3 main.py -d or --database [DATABASE_NAME] -f or --sql_file [SQL_FILE]
python3 main.py -csv or --import_csv [CSV_FILE] -ts or --table_from_sql [TABLE_NAME] -d or --database [DATABASE_NAME]
```

<br>

## Author Information

* Fabiano Santos Florentino [<fabianoflorentino@outlook.com>]
