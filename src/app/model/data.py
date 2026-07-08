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
            """INSERT INTO expenses (catagory_id, amount, creation_date) VALUES (?,?,?)""",
            (formData["category"], formData["amount"], formData["date"]),
        )
        con.commit()
        print(formData)

    def getCategories(self):
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""SELECT * FROM categories""")
        rows = cur.fetchall()
        con.commit()
        return rows
