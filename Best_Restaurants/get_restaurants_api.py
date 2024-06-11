import serpapi
import json
import requests

32.474962, 34.976855
def main():
  client = serpapi.Client(api_key="f9ae0429c9b651cbee59c3229372fadeefe5c448360b1d791b13b099b9baf303")
  result = client.search(
    q="Restaurant",
    engine="google_local",
    num="2",
    type="search",
    location="New York, United States"

  )
  restaurants = result["local_results"]
  restaurants_json = json.dumps(restaurants, indent = 4)
  return restaurants_json

if __name__ == "__main__":
  main()