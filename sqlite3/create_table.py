import sqlite3

sql = '''
CREATE TABLE IF NOT EXISTS persons (
    name text NOT NULL,
    email text UNIQUE NOT NULL, 
    phone text
);
'''

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute(sql)
conn.close()
