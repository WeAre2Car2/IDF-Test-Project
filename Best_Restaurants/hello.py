from flask import Flask
from flask import render_template
from flask import url_for
from restaurants import Restaurant 
# Learning how to use flask
app = Flask(__name__)


@app.route('/')
def hello(name=None):
    name = Restaurant .get_open_status()
    return render_template('hello.html', person=name)
app.run(debug=True)