import sqlite3

DB_NAME = "service_intervals.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS intervals (id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle TEXT NOT NULL, owner TEXT NOT NULL, interval_km INTEGER NOT NULL)")
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)