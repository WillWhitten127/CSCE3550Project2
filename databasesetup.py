# Contents for database_setup.py
import sqlite3

def init_db():
    with sqlite3.connect("keys.db") as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS keys(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key BLOB NOT NULL,
            expired BOOLEAN DEFAULT FALSE
        )
        """)
        conn.commit()

init_db()
