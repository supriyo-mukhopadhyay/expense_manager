import matplotlib.pyplot as plt
import os
from model import data
class report:
    def __init__(self) -> None:
        self.projectPath = os.getcwd()
        self.db = data.database()
    
    def plot(self):
        expenses = self.db.getExpenseData()
        categories = []
        amount = []
        
        for expense in expenses:
            categories.append(expense['name'])
            amount.append(expense['amount'])
            
            
        fig, ax = plt.subplots()
        ax.pie(amount, labels= categories)
        ax.axis('equal')
        # plt.show()
        return fig.savefig(f'{self.projectPath}/src/app/static/img/expenses.png')