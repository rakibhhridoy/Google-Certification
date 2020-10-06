#!/usr/bin/env python3

import os
from PIL import Image

all_images = os.listdir(os.getcwd())

for image_name in all_images:
	path = os.path.join(os.getcwd(), image_name)
	output = os.path.join('/opt/icons/',image_name)

	if 'ic' in path:
		Image.open(path).rotate(270).resize((128,128)).convert('RGB').save(output, 'JPEG')
