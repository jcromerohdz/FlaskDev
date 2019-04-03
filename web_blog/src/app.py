from flask import Flask, render_template, request, session
from models.user import User
from common.database import Database
import sys

app = Flask(__name__) #'__main__'
app.secret_key = "Chris"

@app.route('/')
def hello_method():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    print(email, file=sys.stdout)
    print(password, file=sys.stdout)

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])

if __name__ == '__main__':
    app.run(port=2323, debug=True)
