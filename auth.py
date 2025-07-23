import sqlite3
import bcrypt

def create_user_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 name TEXT,
                 password_hash BLOB)''')
    conn.commit()
    conn.close()

def register_user(username, name, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        c.execute("INSERT INTO users (username, name, password_hash) VALUES (?, ?, ?)",
                  (username, name, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Usuario ya existe
    conn.close()
    return True

def verify_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return False
    stored_hash = row[0]
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
