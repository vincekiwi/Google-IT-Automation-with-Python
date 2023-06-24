#!/usr/bin/env python3

import requests
import os
import json

from_dir = "supplier-data/descriptions/"

text_files = [f for f in os.listdir(from_dir) if f.endswith(".txt")]

def create_json(text_file):
    with open(from_dir + text_file) as f:
        name = f.readline().strip()
        weight = int(f.readline().strip().split()[0])
        description = f.readline().strip()

    item = {
        "name": name,
        "weight": weight,
        "description": description,
        "image_name": text_file.replace(".txt", ".jpeg")
    }

    return item

# Replace with linux instance IP Address
url = "http://localhost/fruits/"
for text_file in text_files:
    data = create_json(text_file)
    response = requests.post(url, json=data)
    print(response.status_code)