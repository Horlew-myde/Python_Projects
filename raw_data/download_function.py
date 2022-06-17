#!usr/bin/env python

import requests

def download(url):
    get_response = requests.get(url)
    print(get_response)

download("file direct url ")


