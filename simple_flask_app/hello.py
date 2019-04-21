from flask import Flask, render_template, request, redirect, url_for, make_response, session

app = Flask(__name__)
# app.secret_key = "super_master_key"
app.config.from_pyfile('settings.py')

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

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # first_name = request.args.get('first_name')
        # last_name = request.args.get('last_name')
        # first_name = request.form.get('first_name')
        # last_name = request.form.get('last_name')
        first_name = request.values.get('first_name')
        last_name = request.values.get('last_name')
        # return f'First name: {first_name}, Last name: {last_name}'
        # response = make_response(redirect(url_for('registered')))
        # response.set_cookie('first_name', first_name)
        session['first_name'] = first_name
        return redirect(url_for('registered'))
    return render_template('form.html')

@app.route('/thank_you')
def registered():
    first_name = session.get('first_name')
    return f'Thank you, {first_name}!'

