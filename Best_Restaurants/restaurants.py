import json

# Creating a restaurant class, each resturant object will hold 1 resturant info
class Restaurant():
   def __init__(self, restaurant_name, restaurant_rating, restaurant_open_status):
      self.restaurant_name = restaurant_name
      self.restaurant_rating = restaurant_rating
      self.restaurant_open_status = restaurant_open_status
 
      










# Opening JSON file
with open('search_example.json', 'r') as openfile:
 
    # Reading from json file
    search_results = json.load(openfile)


def get_ratings():
  ratings_list = []
  for local_result in search_results["local_results"]:
      ratings_list.append(local_result)
      return ratings_list