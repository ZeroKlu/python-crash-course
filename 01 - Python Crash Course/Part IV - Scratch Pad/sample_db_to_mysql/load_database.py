import mysql.connector as mysql
import pandas as pd
from sm_utils import file_path

# MySQL Settings
hostname = "localhost"
username = "python"
password = "training"
database = "ExternalData"

# Database Table Descriptions
tables = {
    "MurphysLaws":{
        "LawID": "smallint NOT NULL PRIMARY KEY",
        "LawName": "varchar(50)",
        "LawText": "varchar(250)"
    },
    "Numbers":{
        "AsNumeral": "varchar(5)",
        "English": "varchar(50)",
        "French": "varchar(50)",
        "Spanish": "varchar(50)",
        "German": "varchar(50)",
        "Italian": "varchar(50)",
        "Greek": "varchar(50)",
        "Latin": "varchar(50)",
        "Japanese": "varchar(50)",
        "Portugese": "varchar(50)",
        "Afrikaans": "varchar(50)",
        "Chinese": "varchar(50)",
        "Irish": "varchar(50)",
        "Norwegian": "varchar(50)",
        "Welsh": "varchar(50)"
    },
    "Phrases":{
        "English": "varchar(50)",
        "French": "varchar(50)",
        "Spanish": "varchar(50)",
        "German": "varchar(50)",
        "Italian": "varchar(50)",
        "Greek": "varchar(50)",
        "Latin": "varchar(50)",
        "Japanese": "varchar(50)",
        "Portugese": "varchar(50)",
        "Afrikaans": "varchar(50)",
        "Chinese": "varchar(50)",
        "Irish": "varchar(50)",
        "Norwegian": "varchar(50)",
        "Welsh": "varchar(50)"
    },
    "ZipCodes":{
        "Id": "int NOT NULL PRIMARY KEY",
        "State": "varchar(20)",
        "County": "varchar(50)",
        "City": "varchar(50)",
        "ZipCode": "varchar(10)",
    }
}

def connect_to_mysql() -> None:
    """Establish connection to MySQL Server"""
    global conn
    conn = mysql.connect(
        host=hostname,
        user=username,
        password=password
    )
    global cmd
    cmd = conn.cursor()
    print("Connected to MySQL...")

def remove_existing_database() -> None:
    """If the ExternalData database already exists, delete it"""
    sql = f"DROP DATABASE IF EXISTS {database}"
    cmd.execute(sql)
    print(f"Removed any existing schema for [{database}]...")

def create_database() -> None:
    """Create and connect to the new ExternalData database"""
    sql = f"CREATE DATABASE {database}"
    cmd.execute(sql)
    print(f"Created new database [{database}]...")
    sql = f"USE {database}"
    cmd.execute(sql)
    print(f"Using database [{database}]...")

def create_tables() -> None:
    """Create tables and columns for the ExternalData database"""
    for table, cols in tables.items():
        print(f"Creating table [{table}]...")
        col_str = ""
        for col, type in cols.items():
            print(f"Adding column [{col}]...")
            if len(col_str) > 0: col_str += ", "
            col_str += f"{col} {type}"
        sql = f"CREATE TABLE {table} ({col_str})"
        cmd.execute(sql)
        print(f"Created table [{table}]...")

def populate_data() -> None:
    """Populate all ExternalData tables from the CSV files"""
    for csv in tables.keys():
        # Note to self: The use of fillna() is needed because in the "Numbers" table, the German and Norwegian for 0 is "NULL",
        #               and pandas is interpreting that as NaN instead of the word "NULL".
        df = pd.read_csv(file_path(f"{csv}.csv"), index_col=False, delimiter=",").fillna("NULL")
        df.head()
        pars = ("%s, " * df.shape[1])
        pars = pars[:len(pars) - 2]
        sql = f"INSERT INTO {csv} VALUES ({pars})"
        for _, row in df.iterrows():
            cmd.execute(sql, tuple(row))
            conn.commit()
        sql = f"SELECT COUNT(*) FROM {csv}"
        cmd.execute(sql)
        for cnt in cmd:
            print(f"Added {cnt} row(s) to {csv}")

def main() -> None:
    """Create and fill my ExternalData MySQL database from the CSV files containing the data from my SQL Server database"""
    connect_to_mysql()
    remove_existing_database()
    create_database()
    create_tables()
    populate_data()

if __name__ == "__main__":
    main()
