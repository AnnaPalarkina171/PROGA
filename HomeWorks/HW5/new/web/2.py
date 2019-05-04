import sqlite3 as lite

con = lite.connect('mydatabase.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM project")
    rows = cur.fetchall()

    for row in rows:
        print(row[1])