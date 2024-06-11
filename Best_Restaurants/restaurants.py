import json

# Creating a restaurant class, each resturant object will hold 1 resturant info
class Restaurant():
  def __init__(self, restaurant_name, restaurant_rating, restaurant_open_status):
    self.restaurant_name = restaurant_name
    self.restaurant_rating = restaurant_rating
    self.restaurant_open_status = restaurant_open_status
    self.resturant_list = []

  # Gets and Sets the values of the object
  def get_restaurant_name(self):
    return self.restaurant_name
  
  def get_restaurant_rating(self):
    return self.restaurant_rating
  
  def get_restaurant_open_status(self):
    return self.restaurant_open_status
  
  def get_restaurant_list(self):
    return self.resturant_list
  
  def add_restaurant(self, restaurant):
    self.resturant_list.append(restaurant)

  # Retrieves the titles from an example JSON file
  def get_titles():
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\search_example.json', 'r') as openfile:
  
      # Reading from json file
      data = json.load(openfile)

    title_list = []
    for result in data["local_results"]:
      title_list.append(result["title"])
    return title_list
  
  # Retrieves the ratings from an example JSON file
  def get_ratings():
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\search_example.json', 'r') as openfile:
  
      # Reading from json file
      data = json.load(openfile)

    rating_list = []
    for result in data["local_results"]:
      rating_list.append(result["rating"])
    return rating_list
  
  # Retrieves the open status from given value, no open status in the JSON example file
  def get_open_status():
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\search_example.json', 'r') as openfile:
  
      # Reading from json file
      data = json.load(openfile)

    is_open_list = []
    for i in range(3):
      is_open_list.append("open") 
    return is_open_list



def main():
  # Creating lists of the attributes
  title_list = Restaurant.get_titles()
  rating_list = Restaurant.get_ratings()
  open_status = Restaurant.get_open_status()
  # Creating a list of restaurant objects
  restaurant_list = []
  for i in range(3):
    restaurant_list.append(Restaurant(title_list[i], rating_list[i], open_status[i]))
    print(restaurant_list[i].get_restaurant_name())
  
     





if __name__ == "__main__":
   main()
