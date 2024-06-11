from flask import Flask
from flask import render_template
from flask import url_for
# Learning how to use flask
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)