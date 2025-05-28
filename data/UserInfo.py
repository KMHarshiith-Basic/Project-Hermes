import sqlite3

ud = sqlite3.connect('data/UserData.db')
c = ud.cursor()

# Ensure the 'players' table exists
'''c.execute(CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    score INTEGER DEFAULT 0
))'''

# Use parameterized queries correctly
def new(n):
    c.execute('INSERT INTO players (username) VALUES (?)', (n,))
    ud.commit()

def id(n):
    c.execute('SELECT id FROM players WHERE username = ?', (n,))
    result = c.fetchone()
    return result[0] if result else None

def check(n):
    c.execute('SELECT * FROM players WHERE username = ?', (n,))
    return c.fetchone() is not None

def dat(I, r1, r2, r3):
    pass
