import json

# Creating a restaurant class, each resturant object will hold 1 resturant info
class Restaurant():
  def __init__(self, restaurant_name, restaurant_rating, restaurant_open_status):
    self.restaurant_name = restaurant_name
    self.restaurant_rating = restaurant_rating
    self.restaurant_open_status = restaurant_open_status
    self.resturant_list = []
  
  @staticmethod
  def sort_JSON(): #sorts the JSON so that the best rating will be on top and saves to a new file!
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\search_example.json', 'r') as openfile:
      # Reading from json file
      data = json.load(openfile)
    # Sort the local_results based on the rating in descending order
    sorted_results = sorted(data['local_results'], key=lambda x: x['rating'], reverse=True)
    # Update the original data with the sorted results
    data['local_results'] = sorted_results
    # Print the sorted data
    with open('Best_Restaurants/sorted_data.json', 'w') as outfile:
      json.dump(data, outfile, indent=2)

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
    
  def get_titles():
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\sorted_data.json', 'r') as openfile:
  
      # Reading from json file
      data = json.load(openfile)

    title_list = []
    for result in data["local_results"]:
      title_list.append(result["title"])
    return title_list
  
  # Retrieves the ratings from an example JSON file
  def get_ratings():
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\sorted_data.json', 'r') as openfile:
      # Reading from json file
      data = json.load(openfile)

    rating_list = []
    for result in data["local_results"]:
      rating_list.append(result["rating"])
    return rating_list
  
  # Retrieves the open status from given value, no open status in the JSON example file
  @staticmethod
  def get_open_status():
    with open('F:\Projects\IDF_Test_Project\Best_Restaurants\sorted_data.json', 'r') as openfile:
  
      # Reading from json file
      data = json.load(openfile)

    is_open_list = []
    for result in data["local_results"]:
      is_open_list.append(result["hours"])
    return is_open_list
  
  @staticmethod
  #takes the lists created earlier and creates
  # a list of restaurants with the data from these lists.
  # prints for debugging
  def get_restaurants(num_of_restaurants):
    # Creating lists of the attributes
    title_list = Restaurant.get_titles()
    rating_list = Restaurant.get_ratings()
    open_status = Restaurant.get_open_status()
    # Creating a list of restaurant objects
    restaurant_list = []
    for i in range(num_of_restaurants):
      restaurant_list.append(Restaurant(title_list[i], rating_list[i], open_status[i]))
      print(f"{restaurant_list[i].get_restaurant_name()}, {restaurant_list[i].get_restaurant_rating()}, {restaurant_list[i].get_restaurant_open_status()}")


def main():
  Restaurant.sort_JSON() 
  Restaurant.get_restaurants(5)

if __name__ == "__main__":
   main()
