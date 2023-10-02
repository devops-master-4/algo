import sqlite3

con = sqlite3.connect("./db/analytics.db")
cur = con.cursor()
# logId, dateId, prodId, catId, fabId
cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
        logID INTEGER PRIMARY KEY AUTOINCREMENT,
        dateID INTEGER,
        prodID INTEGER,
        catID INTEGER,
        fabID INTEGER
    )
''')
con.commit()

# logId, dateId, prodId, catId, fabId, magId

cur.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        logID INTEGER PRIMARY KEY AUTOINCREMENT,
        dateID INTEGER,
        prodID INTEGER,
        catID INTEGER,
        fabID INTEGER,
        magID INTEGER
    )            
''')
con.commit()

cur.execute("SELECT COUNT(*) FROM products")
count = cur.fetchone()[0]

if count == 0:
    print("Database is empty")

    with open('./data/produits-tous.orig', 'r') as data_file:
        for line in data_file:
            parts = line.strip().split()
            if len(parts) == 4:
                dateID, prodID, catID, fabID = map(int, parts)
                cur.execute("INSERT INTO products (dateID, prodID, catID, fabID) VALUES (?, ?, ?, ?)",
                            (dateID, prodID, catID, fabID))
                con.commit()

cur.execute("SELECT COUNT(*) FROM categories")
count = cur.fetchone()[0]

if count == 0:
    print("Database is empty")

    with open('./data/pointsDeVente-tous', 'r') as data_file:
        for line in data_file:
            parts = line.strip().split()
            if len(parts) == 5:
                dateID, prodID, catID, fabID, magID = map(int, parts)
                cur.execute("INSERT INTO categories (dateID, prodID, catID, fabID, magID) VALUES (?, ?, ?, ?, ?)",
                            (dateID, prodID, catID, fabID, magID))
                con.commit()

con.close()
print("Done")