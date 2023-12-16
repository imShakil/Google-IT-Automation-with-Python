#!/usr/bin/python3


#############################
## Author: github@imShakil ##
#############################


import os
from PIL import Image


def change_image(size=(600, 400), dir="./", format="JPEG", format_type='.jpeg'):
    """_summary_

    Args:
        size (tuple, optional): _description_. Defaults to (600, 400).
        dir (str, optional): _description_. Defaults to "/".
        format (str, optional): _description_. Defaults to "JPEG".
        format_type (str, optional): _description_. Defaults to '.jpeg'.
    """
    size = size
    for infile in os.listdir(dir):
        base_name = os.path.abspath(dir+infile)
        file, ext = os.path.splitext(base_name)
        print(file, ext)
        if ext != '.tiff':
            continue
        im = Image.open(base_name)
        #im = im.rotate(90)
        im= im.resize(size)
        jpg_im = im.convert('RGB')
        filename = file + format_type
        print("new image will be saved {}".format(filename))
        jpg_im.save(filename, format=format)

if __name__ == "__main__":
    dir = 'supplier-data/images/'
    change_image(dir=dir)
