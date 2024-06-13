import os

import serpapi
import json
from dotenv import load_dotenv

def main():
  load_dotenv()
  api_key = os.getenv("API_KEY")
  params = {
  "engine": "google_local",
        "engine": "google_maps",
        "type": "search",
        "q": "Restaurant",
        "ll": "@32.4742437,34.993965,15z",
        "google_domain": "google.co.il",
        "hl": "en",
        "gl": "il",
    "api_key": api_key
    #"api_key": "f9ae0429c9b651cbee59c3229372fadeefe5c448360b1d791b13b099b9baf303"
}
  search = serpapi.search(params) # Searches
  results = search.as_dict() # converts to dict
  json_string = json.dumps(results, indent=4)  # to str
  return json_string #returns the str
if __name__ == "__main__":
  main()