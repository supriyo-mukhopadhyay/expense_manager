import matplotlib.pyplot as plt
import os

from numpy import size
from model import data

plt.style.use("bmh")


class report:
    def __init__(self) -> None:
        self.projectPath = os.getcwd()
        self.db = data.database()

    def plot(self, interval="all"):
        expenses = self.db.getExpenseData(interval)
        categories = []
        amount = []

        for expense in expenses:
            categories.append(expense["name"])
            amount.append(expense["amount"])

        fig, ax = plt.subplots()
        # ax.pie(amount, labels=categories)
        # ax.axis("equal")
        ax.bar(categories, amount, label=categories)
        # plt.show()
        return fig.savefig(f"{self.projectPath}/src/app/static/img/expenses.png")


# re = report()
# re.plot()
