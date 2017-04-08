import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, flight TEXT, transport TEXT, food TEXT, entertainment TEXT, living TEXT)')
conn.close()