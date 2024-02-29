from flask import Flask, render_template, redirect, request, session
from datetime import datetime

my_username = "bob"
my_password = "joe"
dummy = [
    {
        "symbol": "sbux",
        "shares": 100,
        "purchase price": 87.65,
        "date": datetime.now(),
        "share price": 102.28,
        "stock position": 10228
    },
    {
        "symbol": "cost",
        "shares": 23,
        "purchase price": 302.17,
        "date": datetime.now(),
        "share price": 373.43,
        "stock position": 8588.89
    },
]


# create the flask application object,
# this object contains all the functions
# and information needed to handle web server
# functionality
app = Flask(__name__)
app.secret_key = b'helloworld'


@app.route("/")
def index():
    username = session.get("username")
    return render_template('index.html', username=username)


@app.route("/list-stocks")
def list_stocks():
    username = session.get("username")
    return render_template("list-stocks.html", dummy=dummy, username=username)


@app.route('/add-stock')
def add_stock():
    username = session.get("username")
    return render_template('add-stock.html', username=username)


@app.route('/profile')
def profile():
    username = session.get('username')
    if not username:
        return redirect("/login")
    return render_template('profile.html', username=username)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == my_username and password == my_password:
            session['username'] = username
            return redirect('/')

    return render_template("login.html")


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=9001)