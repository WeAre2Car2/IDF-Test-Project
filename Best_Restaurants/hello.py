from flask import Flask
from flask import render_template
from flask import url_for
# Learning how to use flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Nadav"):
    return render_template('hello.html', person=name)
app.run()