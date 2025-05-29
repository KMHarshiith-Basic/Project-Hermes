import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'UserData.db')
ud = sqlite3.connect(db_path)
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

def result1(I,u,b):
    R=get_ratings(I)
    r=R[1]
    if r<2000:
        if u==1 and b==1:
            c.execute('UPDATE players SET Rating1 = ? WHERE id = ?', (r+20,I))
            ud.commit()
        elif u==1 and b==0:
            c.execute('UPDATE players SET Rating1 = ? WHERE id = ?', (r+50,I))
            ud.commit()
        elif u==0 and b==1:
            c.execute('UPDATE players SET Rating1 = ? WHERE id = ?', (r-10,I))
            ud.commit()
        elif u==0 and b==0:
            pass # Does not change anything
    else:
        c.execute('UPDATE players SET Rating1 = ? WHERE id = ?', (2000,I))

def result2(I,u,b):
    R=get_ratings(I)
    r=R[2]
    if r<2000:
        if u==1 and b==1:
            c.execute('UPDATE players SET Rating2 = ? WHERE id = ?', (r+20,I))
            ud.commit()
        elif u==1 and b==0:
            c.execute('UPDATE players SET Rating2 = ? WHERE id = ?', (r+50,I))
            ud.commit()
        elif u==0 and b==1:
            c.execute('UPDATE players SET Rating2 = ? WHERE id = ?', (r-10,I))
            ud.commit()
        elif u==0 and b==0:
            pass # Does not change anything
    else:
        c.execute('UPDATE players SET Rating2 = ? WHERE id = ?', (2000,I))

def result3(I,u,b):
    R=get_ratings(I)
    r=R[3]
    if r<2000 and r>100:
        if u==1 and b==1:
            c.execute('UPDATE players SET Rating3 = ? WHERE id = ?', (r+20,I))
            ud.commit()
        elif u==1 and b==0:
            c.execute('UPDATE players SET Rating3 = ? WHERE id = ?', (r+50,I))
            ud.commit()
        elif u==0 and b==1:
            c.execute('UPDATE players SET Rating3 = ? WHERE id = ?', (r-10,I))
            ud.commit()
        elif u==0 and b==0:
            pass # Does not change anything
    elif r>=2000:
        c.execute('UPDATE players SET Rating3 = ? WHERE id = ?', (2000,I))
    else:
        pass