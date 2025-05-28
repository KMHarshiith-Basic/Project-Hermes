import sqlite3

ud = sqlite3.connect('data/UserData.db')
c = ud.cursor()

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

def update(I, r1, r2, r3): # Update player ratings
    c.execute('UPDATE players SET Rating1 = ?, Rating2 = ?, Rating3 = ? WHERE id = ?', (r1, r2, r3, I))
    ud.commit()

def get_data(I):  # Get player data
    c.execute('SELECT * FROM players WHERE id = ?', (I,))
    result = c.fetchone()
    return result if result else None

def get_ratings(I): # Get player ratings
    c.execute('SELECT id, Rating1, Rating2, Rating3 FROM players WHERE id = ?', (I,))
    result = c.fetchone()  
    return result if result else None

print(get_ratings(1))  # Example usage to print data for player with ID 1