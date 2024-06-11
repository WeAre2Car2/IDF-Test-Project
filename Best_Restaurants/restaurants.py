import json

# Creating a restaurant class, each resturant object will hold 1 resturant info
class Restaurant():
  def __init__(self):
    self.restaurant_name = None
    self.restaurant_rating = None
    self.restaurant_open_status = None

  def get_restaurant_name(self):
    return self.restaurant_name
  
  def get_restaurant_rating(self):
     return self.restaurant_rating
  
  def get_restaurant_open_status(self):
     return self.restaurant_open_status
  
  def set_restaurant_name(self, restaurant_name):
    self.restaurant_name = restaurant_name
  
  def set_restaurant_rating(self, restaurant_rating):
     self.restaurant_rating = restaurant_rating
  
  def set_restaurant_open_status(self, restaurant_open_status):
     self.restaurant_open_status = restaurant_open_status



  def get_ratings():
    with open('search_example.json', 'r') as openfile:
  
      # Reading from json file
      data = json.load(openfile)

    title_list = []
    rating_list = []
    is_open_list = []
    for result in data["local_results"]:
      title_list.append(result["title"])
    for result in data["local_results"]:
      rating_list.append(result["rating"])
    for i in range(3):
      is_open_list.append("open")
    print(title_list)
    print(rating_list)
    print(is_open_list)



def main():
  print(Restaurant.get_ratings())
     
     





if __name__ == "__main__":
   main()
