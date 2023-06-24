#!/usr/bin/env python3

from PIL import Image
from os import listdir, path

save_dir = "supplier-data/images"

target_size = (600, 400)
target_format = "jpeg"

images = [f for f in listdir(save_dir) if f.endswith(".tiff")]

for file in images:
    from_image = Image.open(save_dir + "/" + file)
    to_image = from_image.resize(target_size).convert("RGB")
    to_image.save(save_dir + "/" + path.splitext(file)[0] + "." + target_format)