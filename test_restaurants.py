from restaurants import Restaurant

r = Restaurant("Blue", "4.0", "Open")
r2 = Restaurant("Red", "3.5", "Closed")

def test_object_values():
  assert r.get_restaurant_title() == "Blue"
  assert r.get_restaurant_rating() == "4.0"
  assert r.get_restaurant_open_status() == "Open"

title_list = ["Blue", "Red"]
rating_list = ["4.0", "3.5"]
is_open_list = ["Open", "Closed"]

def test_len():
  assert len(Restaurant.get_restaurants(100)) == 20 #Max results per API search
  assert len(Restaurant.get_restaurants(0)) == 0

def test_restaurants_list_values():
  restaurants_list =  Restaurant.get_restaurants(10)
  assert restaurants_list[1].get_restaurant_open_status != None
  assert restaurants_list[4].get_restaurant_title != None


def test_list_values():
  is_open_list = Restaurant.get_open_status()
  assert is_open_list[4] != None
  assert is_open_list[1] != None
