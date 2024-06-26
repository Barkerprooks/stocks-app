import sqlite3
import datetime

def initialize_database():
    db = sqlite3.connect("stocks.db")
    db.execute('CREATE TABLE users (username TEXT UNIQUE, password TEXT, bio TEXT, age NUMBER)')
    db.execute('''CREATE TABLE stocks (
                    symbol TEXT UNIQUE,
                    shares NUMBER,
                    purchase_price REAL,
                    date TEXT,
                    share_price REAL,
                    stock_position NUMBER,
                    userid NUMBER )''')


def create_user(db, username, password):
    db.execute("INSERT INTO users VALUES (?, ?, '', 18)", [username, password])
    db.commit()


def update_user(db, userid, username, bio, age):
    db.execute("UPDATE users SET username = ?, bio = ?, age = ? WHERE rowid = ?", [username, bio, age, userid])
    db.commit()


def check_password(db, username, password):
    result = db.execute("SELECT password FROM users WHERE username = ?", [username])
    stored_password = result.fetchone()[0]
    return stored_password == password


def get_userid(db, username):
    result = db.execute("SELECT rowid FROM users WHERE username = ?", [username])
    return result.fetchone()[0]


def get_bio_and_age(db, username):
    print(username)
    result = db.execute("SELECT bio, age FROM users WHERE username = ?", [username])
    return result.fetchone()


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


def remove_stock(db, symbol, username):
    userid = get_userid(db, username)
    db.execute('DELETE FROM stocks WHERE userid = ? AND symbol = ?', [userid, symbol])
    db.commit()


def get_stocks(db, username):
    userid = get_userid(db, username)
    result = db.execute('SELECT * FROM stocks WHERE userid = ?', [userid])
    return result.fetchall()


if __name__ == "__main__":
    initialize_database()