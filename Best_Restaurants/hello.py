from flask import Flask
from flask import render_template
from flask import url_for
from restaurants import Restaurant 
# Learning how to use flask
app = Flask(__name__)




@app.route('/')
def hello():
    restaurants_names = Restaurant.get_titles()
    restaurants_ratings = Restaurant.get_ratings()
    open_status = Restaurant.get_open_status()
    title1 = restaurants_names[0]
    rating1 = restaurants_ratings[0]
    open_status1 = open_status[0]


    return render_template('hello.html', **locals())
app.run(debug=True)