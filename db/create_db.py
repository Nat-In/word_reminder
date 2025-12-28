import sqlite3
from datetime import datetime

# connect to (create) the database file
conn = sqlite3.connect("wordsdb.sqlite")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS Words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE,
        details TEXT,
        status TEXT,
        created_at DATETIME
    )
    """
)

# save all changes to the database
conn.commit()

# check that the table was created successfully
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())

# close the connection when done
conn.close()
