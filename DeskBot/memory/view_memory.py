import sqlite3
from pathlib import Path


# Find the database
memory_dir = Path(__file__).parent
db_path = memory_dir / "memory.db"

# Connect
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\n=== TABLES ===")
for table in tables:
    print(table[0])

# Display each table's contents
for table in tables:
    table_name = table[0]

    print(f"\n=== {table_name} ===")

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if not rows:
            print("(empty)")
        else:
            for row in rows:
                print(row)

    except Exception as e:
        print(f"Error reading table: {e}")

conn.close()