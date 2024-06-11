import serpapi
import json
import requests

32.474962, 34.976855
def main():
  params = {
  "engine": "google_maps",
  "q": "Restaurant",
  "type": "search",
  "location": "New York, New York, United States",
  "num": "2",
  "api_key": "f9ae0429c9b651cbee59c3229372fadeefe5c448360b1d791b13b099b9baf303"
}
  search = serpapi.search(params)
  results = search.as_dict()
  json_string = json.dumps(results, indent=4)  
  return json_string 

if __name__ == "__main__":
  main()