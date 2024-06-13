import serpapi
import json

def main(): # Parameters to get restaurants in Ny since hebrew doesnt work
  params = {
  "engine": "google_local",
        "engine": "google_maps",
        "type": "search",
        "q": "Restaurant",
        "ll": "@32.4742437,34.993965,15z",
        "google_domain": "google.co.il",
        "hl": "en",
        "gl": "il",
    "api_key": "041287f340959981e1aa3e6ea6a4b4c9721a05422c6e2ccc476dc91320c744a5"
    #"api_key": "f9ae0429c9b651cbee59c3229372fadeefe5c448360b1d791b13b099b9baf303"
}
  search = serpapi.search(params) # Searches
  results = search.as_dict() # converts to dict
  json_string = json.dumps(results, indent=4)  # to str
  return json_string #returns the str
if __name__ == "__main__":
  main()