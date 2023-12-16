#! /usr/bin/env python3


import os
import requests


def upload(req_url, data):
    try:
        r = requests.post(url=req_url, json=data)
    except Exception as e:
        print(e)
        return e


def process_json_data(dir="./"):
    """_summary_

    Args:
        files (_type_): _description_
        dir (str, optional): _description_. Defaults to "./".
    """
    json_data_list = []

    for file in os.listdir(dir):
        print(file)
        filename, ext = os.path.splitext(os.path.basename(file))
        if ext == '.txt':
            lines = open(dir + file, 'r').read().split('\n')
            data = dict()
            data['name'] = lines[0]
            data['weight'] = int(lines[1].split(' ')[0])
            data['description'] = lines[2]
            data['image_name'] = filename + ".jpeg"
            json_data_list.append(data)
    return json_data_list
    

if __name__ == "__main__":
    dir = 'supplier-data/descriptions/'
    json_data = process_json_data(dir)
    print(json_data)
    for item in json_data:
        print('uploading {}'.format(item))
        upload(req_url='http://34.74.64.48/fruits/', data=item)
