#!/usr/bin/python3


#############################
## Author: github@imShakil ##
#############################


import os, glob
from PIL import Image

size = (128, 128)
dir = "/opt/icons/"

for infile in glob.glob('images/*'):
    base_name = os.path.basename(infile)
    file, ext = os.path.splitext(base_name)
    print(base_name)
    print(file, ext)
    im = Image.open(infile)
    im = im.rotate(90)
    im= im.resize(size)
    jpg_im = im.convert('RGB')
    jpg_im.save(dir + file, format='JPEG')

