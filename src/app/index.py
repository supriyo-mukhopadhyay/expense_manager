from flask import Flask, render_template, request
import os
from model import data

db = data.database()

projectPath = os.getcwd()
app = Flask(__name__, template_folder=f"{projectPath}/src/app/templates/")


@app.route("/")
def enpenseForm():
    categories = db.getCategories()
    return render_template("index.html", categories=categories)


@app.route("/save", methods=["POST"])
def saveEnpenseForm():
    db.saveExpense(request.form)
    return render_template("index.html")


app.run(port=8080, debug=True)
