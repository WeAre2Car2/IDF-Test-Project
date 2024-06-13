from flask import Flask
from flask import render_template
from flask import url_for
from restaurants import Restaurant 
# Learning how to use flask
app = Flask(__name__)

Restaurant.sort_JSON() 
NUM_OF_RESTAURANTS = 10 # Constant, should not change
restaurant_list = Restaurant.get_restaurants(NUM_OF_RESTAURANTS)


@app.route('/')
def homepage():

    return render_template('index.html', length = len(restaurant_list), restaurant_list = restaurant_list)
app.run(debug=True)

# docker run -p 5000:5000