from math import e

from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import os
from model import data
from visualization import plots

db = data.database()
pt = plots.report()
projectPath = os.getcwd()
app = Flask(
    __name__,
    template_folder=f"{projectPath}/src/app/templates/",
    static_folder=f"{projectPath}/src/app/static",
)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SESSION_PERMANENT"] = False  # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"  # Store session data in files
# Initialize Flask-Session
Session(app)


@app.route("/", methods=["GET", "POST"])
def loginForm():
    if request.method == "POST":
        formData = request.form.to_dict(flat=True)
        userData = db.getUserData(formData["email"], formData["password"])
        print(userData)
        if len(userData) >= 1:
            print(request.form.get("name"))
            # session["name"] = request.form.get("name")
            session["user_id"] = userData[0]
            session["user_name"] = userData[1]
            session["email"] = userData[2]

            return render_template("dashboard.html", userData=userData)
    return render_template("login.html")


@app.route("/addexpense", methods=["GET", "POST"])
def addExpenseForm():
    if not session.get("user_id"):
        return redirect("/")
    if request.method == "POST":
        formData = request.form.to_dict(flat=True)
        print(formData)
        if request.form["category_id"] == "other":
            category_id = db.insertCategory(request.form["other"])
            formData["category_id"] = category_id  # type: ignore
            print(formData)

        db.saveExpense(formData, session["user_id"])
    categories = db.getCategories()

    return render_template("addexpense.html", categories=categories)


@app.route("/reports", methods=["GET", "POST"])
def renderReports():
    if not session.get("user_id"):
        return redirect("/")
    try:
        if request.method == "POST":
            interval = request.form.get("interval")
            pt.plot(interval)  # type: ignore
            print(interval)
    except Exception as e:
        print(e)
    return render_template("reports.html")


@app.route("/DailyReports", methods=["GET"])
def renderDailyReports():
    if not session.get("user_id"):
        return redirect("/")
    try:
        if request.method == "GET":
            pt.plot("daily")
        else:
            pt.plot()
    except Exception as e:
        print(e)
    return render_template("reports.html")


@app.route("/weeklyReports", methods=["GET"])
def renderWeeklyReports():
    if not session.get("user_id"):
        return redirect("/")
    try:
        if request.method == "GET":
            pt.plot("weekly")
        else:
            pt.plot()
    except Exception as e:
        print(e)
    return render_template("reports.html")


@app.route("/monthlyReports", methods=["GET"])
def renderMonthlyReports():
    if not session.get("user_id"):
        return redirect("/")
    try:
        if request.method == "GET":
            pt.plot("monthly")
        else:
            pt.plot()
    except Exception as e:
        print(e)
    return render_template("reports.html")


@app.route("/save", methods=["GET", "POST"])
def save():
    if not session.get("user_id"):
        return redirect("/")
    print("hi")
    return render_template("dashboard.html")


@app.route("/yearlyReports", methods=["GET"])
def renderYearlyReports():
    if not session.get("user_id"):
        return redirect("/")
    try:
        if request.method == "GET":
            pt.plot("yearly")
        else:
            pt.plot()
    except Exception as e:
        print(e)
    return render_template("reports.html")


@app.route("/user", methods=["GET", "POST"])
def userDetails():
    if not session.get("user_id"):
        return redirect("/")
    fname = session["user_name"].split()[0]
    lname = session["user_name"].split()[1]

    email = session["email"]
    id = session["user_id"]
    return render_template(
        "userdetails.html", fname=fname, lname=lname, email_addr=email, id=id
    )


@app.route("/home", methods=["GET", "POST"])
def home():
    if not session.get("user_id"):
        return redirect("/")
    return render_template("dashboard.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session["user_id"] = None
    session["user_name"] = None
    session["email"] = None

    return redirect("/")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
