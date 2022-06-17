#!usr/bin/env python

import requests


def download(url):
    get_response = requests.get(url)
    # print(get_response)
    # with open("sample.txt", "r/w/rw")
    # with open("sample.txt", "w") as out_file:
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
    # with open("sample.txt", "wb") as out_file:
        # out_file.write("this is a text")
        out_file.write(get_response.content)

download("file direct url ")

