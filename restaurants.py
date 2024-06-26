import json
import get_restaurants_api as json_get

# Creating a restaurant class, each resturant object will hold 1 resturant info
class Restaurant():
  def __init__(self, restaurant_title, restaurant_rating, restaurant_open_status):
    self.restaurant_title = restaurant_title
    self.restaurant_rating = restaurant_rating
    self.restaurant_open_status = restaurant_open_status
  
  def sort_JSON(): #sorts the JSON so that the best rating will be on top and saves to a new file!
    data = json_get.main() # Loads to string
    data_json = json.loads(data) # Converts to json
    # Sort the local_results based on the rating in descending order
    sorted_results = sorted(data_json['local_results'], key=lambda x: x.get('rating', 0), reverse=True)
    # Update the original data with the sorted results
    data_json['local_results'] = sorted_results
    # Returns the sorted data
    return data_json

  # Gets and Sets the values of the object
  def get_restaurant_title(self):
    return self.restaurant_title
  
  def get_restaurant_rating(self):
    return self.restaurant_rating
  
  def get_restaurant_open_status(self):
    return self.restaurant_open_status
  
  def get_restaurant_list(self):
    return self.resturant_list
  
  def add_restaurant(self, restaurant):
    self.resturant_list.append(restaurant)
    
  def get_titles():
    data = Restaurant.sort_JSON()
    title_list = [result["title"] for result in data["local_results"]]
    return title_list
  
  # Retrieves the ratings from an example JSON file
  def get_ratings():
    data = Restaurant.sort_JSON()
    #Gives The rating out of the json file, and no rating if the api didnt return any
    rating_list = [result.get("rating", "No Rating!") for result in data["local_results"]] 
    return rating_list
  
  # Retrieves the open status from given value, no open status in the JSON example file
  def get_open_status():
    data = Restaurant.sort_JSON()
    #Gives The opening hours and if its open out of the json file, and "Unknown" if the api didnt return any
    is_open_list = [result.get("hours", "Unknown") for result in data["local_results"]]
    return is_open_list
  
  #takes the lists created earlier and creates
  # a list of restaurant objects with the data from these lists.
  def get_restaurants(num_of_restaurants):
    # Creating lists of the attributes
    title_list = Restaurant.get_titles()
    rating_list = Restaurant.get_ratings()
    open_status = Restaurant.get_open_status()
    # Creating a list of restaurant objects
    restaurant_list = []
    try:
      for i in range(num_of_restaurants):
        restaurant_list.append(Restaurant(title_list[i], rating_list[i], open_status[i]))
    
    except IndexError:
      print("Out Of Bounds")
    return restaurant_list

def main():
  pass

if __name__ == "__main__":
   main()
