#list of packages and documentation at pypi.org
# pypi.org/project/cowsay
# pypi.org/project/requests
import requests
import json
import sys


response = requests.get("https://itunes.apple.com/search?&entity=song&limit=10&term="+sys.argv[1])
#print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    if result["primaryGenreName"]=="Telugu":
        print(result["trackName"], result["artistName"] )

response = requests.get(f"https://itunes.apple.com/search?&entity=song&limit=20&term={sys.argv[1]}&term={sys.argv[2]}")
#print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    if result["primaryGenreName"]=="Telugu":
        print("song: ", result["trackName"], "artist: ", result["artistName"], sep = " ")

