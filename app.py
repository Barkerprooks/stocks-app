from flask import Flask, render_template

# create the flask application object,
# this object contains all the functions
# and information needed to handle web server
# functionality
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list-stocks")
def list_stocks():
    return render_template("list-stocks.html")

@app.route('/add-stock')
def add_stock():
    return render_template('add-stock.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    return "you cant even log in tho <a href='/'>home</a>"


if __name__ == "__main__":
    app.run(debug=True, port=9001)