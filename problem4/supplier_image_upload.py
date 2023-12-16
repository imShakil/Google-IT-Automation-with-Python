#!/usr/bin/env python3


import os
import requests

# This example shows how a file can be uploaded using
# The Python Requests module


def upload(dir='./', req_url="https://example.com/upload"):
    for file in os.listdir(dir):
        file = os.path.abspath(dir + file)
        filename, ext = os.path.splitext(file)
        print(filename, ext)
        if ext == '.jpeg':
            with open(file, 'rb') as data:
                try:
                    print('Uploading {}'.format(file))
                    r = requests.post(url=req_url, files= {'file': data})
                except Exception as e:
                    print(e)
                    return e


if __name__ == "__main__":
    req_url = 'http://34.74.64.48/upload/'
    dir = 'supplier-data/images/'
    upload(dir=dir, req_url=req_url)

