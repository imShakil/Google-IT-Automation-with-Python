#!/usr/bin/env python3

import changeImage
import reports
import supplier_image_upload
import report_email
import run
import sys

# change Image format and resize
# Size: Change image resolution from 3000x2000 to 600x400 pixel
# Format: Change image format from .TIFF to .JPEG


# solution 1

def main(args):
    print(args)
    print(type(args))
    print(type(args[0]))


main(sys.argv)
