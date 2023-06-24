#!/usr/bin/env python3

import requests
from os import listdir

# Add linux instance IP address here
url = ".../upload/"

def upload_file(file_name, url):
    with open(file_name, "rb") as f:
        files = {"file": f}
        requests.post(url, files={"file": opened})

save_dir = "supplier-data/images/"

image_files = [save_dir + file for file in listdir(save_dir) if file.endswith(".jpeg")]

for image in image_files:
    upload_file(image, url)