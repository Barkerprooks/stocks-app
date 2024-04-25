from flask import Flask, g, render_template, redirect, request, session
from datetime import datetime
import sqlite3
import database


def get_db():
    if db := getattr(g, '_database', None) is None:
        db = g._database = sqlite3.connect("stocks.db")
    return db


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
    username = session.get('username')
    if not username:
        return redirect("/login")
    
    db = get_db()
    stocks = database.get_stocks(db, username)

    return render_template("list-stocks.html", stocks=stocks, username=username)


@app.route('/add-stock', methods=["GET", "POST"])
def add_stock():
    username = session.get('username')
    if not username:
        return redirect('/login')
    
    if request.method == 'POST':
        db = get_db()
        symbol = request.form['symbol']
        shares = request.form['shares']
        purchase_price = request.form['purchase_price']
        share_price = request.form['share_price']
        stock_position = request.form['stock_position']

        userid = database.get_userid(db, username)
        database.create_stock(db, symbol, shares, purchase_price, share_price, stock_position, userid)

    return render_template('add-stock.html', username=username)


@app.route('/profile')
def profile():
    username = session.get('username')
    if not username:
        return redirect("/login")
    return render_template('profile.html', username=username)


@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        db = get_db()
        username = request.form['username']
        password = request.form['password']
        database.create_user(db, username, password)
        return redirect('/login')
    return render_template("create.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = get_db()
        username = request.form['username']
        password = request.form['password']
        if database.check_password(db, username, password):
            session['username'] = username
            return redirect('/')
    return render_template("login.html")


@app.route('/delete/<symbol>')
def delete(symbol):
    username = session.get('username')
    if not username:
        return redirect('/')
    
    db = get_db()
    database.remove_stock(db, symbol, username)

    return redirect('/list-stocks')



@app.route('/logout')
def logout():
    if session.get('username'):
        del session['username']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=9001)