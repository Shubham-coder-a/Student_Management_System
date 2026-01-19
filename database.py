import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
