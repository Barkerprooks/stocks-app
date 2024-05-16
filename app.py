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

    db = get_db()
    bio, age = '', 18
    if username:
        bio, age = database.get_bio_and_age(db, username)

    return render_template('index.j2', username=username, age=age, bio=bio)


@app.route("/list-stocks")
def list_stocks():
    username = session.get('username')
    if not username:
        return redirect("/login")
    
    db = get_db()
    stocks = database.get_stocks(db, username)

    return render_template("list-stocks.j2", stocks=stocks, username=username)


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

    return render_template('add-stock.j2', username=username)


@app.route('/profile', methods=["GET", "POST"])
def profile():
    username = session.get('username')
    if not username:
        return redirect("/login")
    
    db = get_db()
    bio, age = database.get_bio_and_age(db, username)

    if request.method == "POST":
        userid = database.get_userid(db, username)
        
        username = session['username'] = request.form['username']
        
        bio = request.form['bio']
        age = int(request.form['age'])
        database.update_user(db, userid, username, bio, age)


    return render_template('profile.j2', username=username, bio=bio, age=age)


@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        db = get_db()
        username = request.form['username']
        password = request.form['password']
        database.create_user(db, username, password)
        return redirect('/login')
    
    return render_template("create.j2")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = get_db()
        username = request.form['username']
        password = request.form['password']
        if database.check_password(db, username, password):
            session['username'] = username
            return redirect('/')
    return render_template("login.j2")


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



@app.route("/calc", methods=["GET", "POST"])
def calc():

    answer = 0
    if request.method == "POST":
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        answer = num1 * num2

    return render_template("calc.j2", answer=answer)



if __name__ == "__main__":
    app.run(debug=True, port=9001)