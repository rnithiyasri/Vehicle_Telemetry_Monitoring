import sqlite3

DB_NAME = "vehicle_telemetry.db"

def create_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        speed REAL,
        fuel REAL,
        engine_temp REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_data(speed, fuel, engine_temp):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO telemetry (speed, fuel, engine_temp)
    VALUES (?, ?, ?)
    """, (speed, fuel, engine_temp))

    conn.commit()
    conn.close()
