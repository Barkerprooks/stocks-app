import sqlite3
import datetime

def initialize_database():
    db = sqlite3.connect("stocks.db")
    db.execute('CREATE TABLE users (username TEXT UNIQUE, password TEXT)')
    db.execute('''CREATE TABLE stocks (
                    symbol TEXT,
                    shares NUMBER,
                    purchase_price REAL,
                    date NUMBER,
                    share_price REAL,
                    stock_position NUMBER 
                    userid NUMBER )''')


def create_user(db, username, password):
    db.execute("INSERT INTO users VALUES (?, ?)", [username, password])
    db.commit()


def check_password(db, username, password):
    result = db.execute("SELECT password FROM users WHERE username = ?", [username])
    stored_password = result.fetchone()[0]
    return stored_password == password


def create_stock(db, symbol, shares, purchase_price, share_price, stock_position, userid):
    date = datetime.date.today()
    
    fields = [ 
        symbol, 
        shares, 
        purchase_price, 
        date.strftime('%D'), 
        share_price, 
        stock_position,
        userid
    ]

    db.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)", fields)
    db.commit()


if __name__ == "__main__":
    initialize_database()