import json

# Creating a resturant class, each resturant object will hold 1 resturant info
class Restaurant():
   def __init__(self, resturant_name, resturant_rating, resturant_open_status):
      self.resturant_name = resturant_name
      self.resturant_rating = resturant_rating
      self.resturant_open_status = resturant_open_status
 
      










# Opening JSON file
with open('search_example.json', 'r') as openfile:
 
    # Reading from json file
    search_results = json.load(openfile)


def get_ratings():
  ratings_list = []
  for local_result in search_results["local_results"]:
      ratings_list.append(local_result)
      return ratings_list