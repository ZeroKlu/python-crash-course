"""Validate that the DB is created and loaded"""

import mysql.connector as mysql

# MySQL Settings
hostname = "localhost"
username = "python"
password = "training"
database = "ExternalData"

# Database Table Names
tables = ["MurphysLaws", "Numbers", "Phrases", "ZipCodes"]

def main() -> None:
    """Check that I filled my ExternalData MySQL database properly"""

    my_db = mysql.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    my_cursor = my_db.cursor()

    for table in tables:
        my_cursor.execute(f"SELECT COUNT(*) FROM {table}")
        print(f"{table} contains {my_cursor.fetchone()[0]} row(s)")
        my_cursor.execute(f"SELECT * FROM {table} LIMIT 5")
        print("First Five Rows")
        print("---------------")
        for row in my_cursor.fetchall():
            print("-", row)
        print()

if __name__ == "__main__":
    main()
