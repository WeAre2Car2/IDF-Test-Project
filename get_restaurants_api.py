import serpapi
import json

def main(): # Parameters to get restaurants in Ny since hebrew doesnt work
  params = {
  "engine": "google_local",
        "q": "Restaurant",
        "location_requested": "Tel Aviv Yafo, Israel",
        "location_used": "Tel Aviv-Yafo,Tel Aviv District,Israel",
        "google_domain": "google.com",
        "hl": "en",
        "gl": "il",
        "device": "desktop",
  "api_key": "f9ae0429c9b651cbee59c3229372fadeefe5c448360b1d791b13b099b9baf303"
}
  search = serpapi.search(params) # Searches
  results = search.as_dict() # converts to dict
  json_string = json.dumps(results, indent=4)  # to str
  return json_string #returns the str
if __name__ == "__main__":
  main()