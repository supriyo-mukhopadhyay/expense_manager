from flask import Flask, render_template, request, redirect, url_for
import os
from model import data
from visualization import plots


db = data.database()
pt = plots.report()
projectPath = os.getcwd()
app = Flask(__name__, template_folder=f"{projectPath}/src/app/templates/", static_folder=f"{projectPath}/src/app/static")


@app.route("/", methods=["GET", "POST"])
def enpenseForm():
    if request.method == "POST":
        formData = request.form.to_dict(flat=True)
        print(formData)
        if request.form["category_id"] == "other":
            category_id = db.insertCategory(request.form["other"])
            formData["category_id"] = category_id # type: ignore
            print(formData)
        
        db.saveExpense(formData)
    categories = db.getCategories()    
    return render_template("index.html", categories=categories)

@app.route("/report")
def report():
    pt.plot()
    return render_template("report.html")

app.run(port=8080, debug=True)
