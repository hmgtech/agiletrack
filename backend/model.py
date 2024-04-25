import sqlite3

DATABASE = 'AgileTrack.db'

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            columns TEXT,
            tasks TEXT,
            title TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_boards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            board_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (board_id) REFERENCES boards(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS board_owners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            board_id INTEGER,
            owner_id INTEGER,
            FOREIGN KEY (board_id) REFERENCES boards(id),
            FOREIGN KEY (owner_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
