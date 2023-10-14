from flet import *
import sqlite3


def main(page: Page):

    a = TextField(label="Login", border=InputBorder.UNDERLINE)
    b = TextField(label="Password", border=InputBorder.UNDERLINE)
    page.add(a)
    page.add(b)
    page.add(TextButton("Login"))

    con = sqlite3.connect("data.db")
    cur = con.cursor()

    for i in cur.execute("select * from admin"):
        page.add(Text(f"{i}"))
        page.update()


app(main, view=WEB_BROWSER)
