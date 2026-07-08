import sqlite3
import os

projectPath = os.getcwd()


def create_table():
    con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")

    con.execute(
        """CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT)"""
    )
    con.execute(
        """CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, catagory_id INTEGER, amount INTEGER, creation_date TEXT, FOREIGN KEY (catagory_id) REFERENCES categories (id))"""
    )

    print("table created suucessfully")
    con.close()


def insertDefaultData():
    con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO categories (name) VALUES ("Travel")""")
    cur.execute("""INSERT INTO categories (name) VALUES ("Food")""")
    cur.execute("""INSERT INTO categories (name) VALUES ("Medical")""")
    con.commit()
    con.close()
    print("default data inserted")


def resetDatabase():
    con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
    con.execute("""DROP TABLE expenses""")
    con.execute("""DROP TABLE categories""")
    con.close()


# resetDatabase()
# create_table()
insertDefaultData()
