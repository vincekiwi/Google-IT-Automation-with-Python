#!/usr/bin/env python3
from PIL import Image
from os import listdir

from_dir = "images/"
to_dir = "/opt/icons/"

target_rotate = -90
target_size = (128, 128)
target_format = "JPEG"

target_files = [filename for filename in listdir(from_dir) if filename.startswith("ic_")]

for target_file in target_files:
    print("Processing " + target_file)
    from_image = Image.open(from_dir + target_file)
    target_image = from_image.rotate(target_rotate).resize(target_size).convert("RGB")
    target_image.save(to_dir + target_file, target_format)