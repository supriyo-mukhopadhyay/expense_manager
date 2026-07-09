import sqlite3
from tkinter import NO
from datetime import datetime, date

import os

projectPath = os.getcwd()


class database:
    def __init__(self) -> None:
        pass

    def saveExpense(self, formData, user_id) -> None:
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        cur = con.cursor()
        dtime = datetime.strptime(formData["date"], "%Y-%m-%dT%H:%M")
        print(dtime.strftime("%Y-%m-%d"))
        cur.execute(
            """INSERT INTO expenses (category_id, amount, creation_date, user_id) VALUES (?,?,?,?)""",
            (
                formData["category_id"],
                formData["amount"],
                dtime.strftime("%Y-%m-%d"),
                user_id,
            ),
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

    def getExpenseData(self, interval):
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        query = self.getIntervalQuery()[interval]
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        return rows

    def getUserData(self, email="", password=""):
        con = sqlite3.connect(f"{projectPath}/data/external/expenseManager.db")
        cur = con.cursor()
        # query1 = """SELECT * FROM users WHERE email = \"supriyo.sam999@gmail.com\" and password = \"123\""""
        query = f"""SELECT * FROM users WHERE email = \"{email}\" and password = \"{password}\""""
        cur.execute(query)
        con.commit()
        result = cur.fetchone()
        con.close()
        return result

    def getIntervalQuery(self):
        return {
            "all": """SELECT SUM(e.amount) as amount, c.name FROM expenses as e JOIN categories as c ON e.category_id = c.id GROUP BY c.name""",
            "daily": """SELECT SUM(e.amount) as amount, c.name FROM expenses as e JOIN categories as c ON e.category_id = c.id WHERE e.creation_date = date('now','localtime') GROUP BY c.name""",
            "weekly": """SELECT SUM(e.amount) as amount, c.name FROM expenses as e JOIN categories as c ON e.category_id = c.id WHERE e.creation_date >= date('now','-7 days') GROUP BY c.name""",
            "monthly": """SELECT SUM(e.amount) as amount, c.name FROM expenses as e JOIN categories as c ON e.category_id = c.id WHERE e.creation_date >= date('now','-1 month') GROUP BY c.name""",
            "yearly": """SELECT SUM(e.amount) as amount, c.name FROM expenses as e JOIN categories as c ON e.category_id = c.id WHERE e.creation_date >= date('now','1 year') GROUP BY c.name""",
        }


# db = database()
# print(db.getUserData())
