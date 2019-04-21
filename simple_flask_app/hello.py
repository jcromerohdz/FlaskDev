from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting/<name>')
def greeting(name):
    # return 'Hello ' + name
    return render_template('name.html', t_name=name)

