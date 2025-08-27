import json
import requests
import sys

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term="+sys.argv[1])

#print (json.dumps(response.json(), indent = 2))

o = response.json()

print(f"Results found: {o["resultCount"]}")

for result in o["results"]:
    print (f"Track: {result["trackName"]}, *** Collection: {result["collectionCensoredName"]}")