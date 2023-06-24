'''
import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

    
 with open('people.json', 'r') as people_json:
     people = json.load(people_json)

import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

import requests
response = requests.get('https://www.google.com')
response.raise_for_status()

response.request.headers['Accept-Encoding']

response.ok

response.status_code


p = {"search": "grey kitten",
      "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url

p = {"description": "white kitten",
      "name": "Snowball",
      "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)


response = requests.post("https://example.com/path/to/api", json=p)
response.request.url
'https://example.com/path/to/api'
response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 

'''


#! /usr/bin/env python3

import json
import requests
import os

from_file = "feedback/"

all_files = os.listdir(from_file)

def read_file(filename):
    with open(from_file + filename, 'r') as f:
        return f.read().splitlines()

reviews = []
keys = ["title", "name", "date", "feedback"]

for file in all_files:
    lines = read_file(file)
    reviews.append(dict(zip(keys, lines)))

url = "http://35.184.91.120/feedback/"

for review in reviews:
    response = requests.post(url, data=review)
    response.raise_for_status()
    print("review added")