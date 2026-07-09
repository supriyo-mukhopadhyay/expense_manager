import sqlite3
import os
import datetime

projectPath = os.getcwd()


def create_table():
    con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")

    con.execute(
        """CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT)"""
    )
    con.execute(
        """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)"""
    )
    con.execute(
        """CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, category_id INTEGER, amount INTEGER, creation_date TEXT, user_id INTEGER, FOREIGN KEY (category_id) REFERENCES categories (id), FOREIGN KEY (user_id) REFERENCES users (id))"""
    )

    print("table created suucessfully")
    con.close()


def insertDefaultData():
    con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO categories (name) VALUES ("Travel")""")
    cur.execute("""INSERT INTO categories (name) VALUES ("Food")""")
    cur.execute("""INSERT INTO categories (name) VALUES ("Medical")""")

    cur.execute(
        """INSERT INTO users (name,email,password) VALUES ("Supriyo Mukhopadhyay","supriyo.sam999@gmail.com","123")"""
    )

    cur.execute(
        """INSERT INTO users (name,email,password) VALUES ("Rohit Raj","rohit.sam999@gmail.com","123")"""
    )

    cur.execute(
        """INSERT INTO users (name,email,password) VALUES ("Ananya M","ananya.sam999@gmail.com","123")"""
    )

    con.commit()
    con.close()
    print("default data inserted")


def resetDatabase():
    con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
    con.execute("""DROP TABLE expenses""")
    con.execute("""DROP TABLE categories""")
    con.execute("""DROP TABLE users""")
    con.close()


resetDatabase()
create_table()
insertDefaultData()
