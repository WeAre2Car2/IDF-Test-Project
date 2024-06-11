from flask import Flask
from flask import render_template
from flask import url_for
from restaurants import Restaurant 
# Learning how to use flask
app = Flask(__name__)

restaurant_list = Restaurant.get_restaurants(5)


@app.route('/')
def homepage():
    
    return render_template('index.html', length = len(restaurant_list), restaurant_list = restaurant_list)
app.run(debug=True)