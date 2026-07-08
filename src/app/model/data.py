import sqlite3
from tkinter import NO


import os

projectPath = os.getcwd()


class database:
    def __init__(self) -> None:
        pass

    def saveExpense(self, formData) -> None:
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO expenses (category_id, amount, creation_date) VALUES (?,?,?)""",
            (formData["category_id"], formData["amount"], formData["date"]),
        )
        con.commit()
        print(formData)

    def getCategories(self):
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""SELECT * FROM categories""")
        rows = cur.fetchall()
        con.close()
        return rows

    def insertCategory(self, name):
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO categories (name) VALUES (?)""", [name])
        con.commit()
        insertid = cur.lastrowid
        con.close()
        return insertid

    def getExpenseData(self):
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT SUM(e.amount) as amount, c.name FROM expenses as e JOIN categories as c ON e.category_id = c.id GROUP BY c.name")
        rows = cur.fetchall()
        con.close()
        return rows