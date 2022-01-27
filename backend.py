import sqlite3

def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookinventory (id integer primary key, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookinventory")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookinventory where title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def add(title, author, year, isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookinventory VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def update(title, author, year, isbn, id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookinventory set title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookinventory where id=?", (id,))
    conn.commit()
    conn.close()



connect()
#add("The Alchamist", "Paul Walker", 1996, 7895689)
#update('How to make you thick', 'Bhale Carniage', 1972, 9895689,2)
#delete(2)
##print(view())
##print(search(year=1996))
