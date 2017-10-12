"""
Vivien Lee, Joyce Wu
SoftDev1 Pd7
HW08 - Do I Know You?
2017-10-10
"""

import os
from flask import Flask, render_template, request, session, redirect, url_for, redirect, flash

app = Flask(__name__)
#generates a random 32-bit string to act as the key
app.secret_key = os.urandom(32)
#hardcoded username and password
username = "dog"
password = "cat"
SUCCESS = 1
BAD_PASS = -1
BAD_USER = -2

def auth(user, passw):
    if user == username:
        if passw == password:
            return SUCCESS
        else:
            return BAD_PASS
    else:
        return BAD_USER

@app.route("/", methods=["POST","GET"])
def login():
    #if logged in, redirect to welcome page
    if("username" in session.keys()):
        return redirect(url_for("welcome_page"))
    #if not logged, login template rendered
    return render_template("login.html", loginfailed = "")

@app.route("/login", methods=["POST","GET"])
def checklogin():
    '''
    #wrong username
    if request.form["user"] != username:
        return render_template("login.html", loginfailed = "Wrong username!")
    #wrong password
    if request.form["pass"] != password:
        return render_template("login.html", loginfailed = "Wrong password!")
    #correct login, directs to welcome page
    '''

    result = auth(request.form["user"], request.form["pass"])
    flash("what?")
    if result == SUCCESS:
        session["username"] = request.form["user"]
        return redirect(url_for("welcome_page"))
    if result == BAD_PASS:
        flash("password")
        return render_template("login.html", loginfailed = "Wrong password!")
    if result == BAD_USER:
        flash("user")
        return render_template("login.html", loginfailed = "Wrong password!")

@app.route("/welcome", methods=["POST","GET"])
def welcome_page():
    #checks if logged in
    if "username" in session.keys():
        return render_template("welcome.html", user_name = session["username"])
    else:
        flash("do they think they can get away without logging in?")
        return render_template("login.html", loginfailed= "Please login!")

@app.route("/logout", methods=["POST","GET"])
def logout():
    session.pop("username")
    #redirects to login page
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()
