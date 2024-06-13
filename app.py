from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from restaurants import Restaurant 
# Learning how to use flask
app = Flask(__name__)

Restaurant.sort_JSON() 
NUM_OF_RESTAURANTS = 10 # Constant, should not change
restaurant_list = Restaurant.get_restaurants(NUM_OF_RESTAURANTS)

# Redirects all paths do homepage()
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('homepage'))

# Handles error
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('homepage'))

@app.route('/')
def homepage():

    return render_template('index.html', length = len(restaurant_list), restaurant_list = restaurant_list)
app.run(debug=True)

# docker run -p 5000:5000