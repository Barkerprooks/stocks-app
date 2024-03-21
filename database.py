import sqlite3

def initialize_database():
    db = sqlite3.connect("stocks.db")
    db.execute('CREATE TABLE users (username TEXT UNIQUE, password TEXT)')
    db.execute('''CREATE TABLE stocks (
                    symbol TEXT,
                    shares NUMBER,
                    purchase_price REAL,
                    date NUMBER,
                    share_price REAL,
                    stock_position NUMBER )''')

def create_user(db, username, password):
    db.execute("INSERT INTO users VALUES (?, ?)", [username, password])
    db.commit()

def check_password(db, username, password):
    result = db.execute("SELECT password FROM users WHERE username = ?", [username])
    stored_password = result.fetchone()[0]
    return stored_password == password

if __name__ == "__main__":
    initialize_database()