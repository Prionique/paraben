from sqlite3 import *

con = connect("data.db")
cur = con.cursor()

a = ("primon", "123")
cur.execute("insert into admin values (?,?)", a)
con.commit()