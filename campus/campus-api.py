#!/usr/bin/python3
import urllib.request
from os import listdir
from pprint import pprint
import json
import re

url = 'https://www.campus.co/api/campuses/madrid/events/v2'


def get_url_campus(url):
    urllib.request.urlretrieve(url, './campus.json')

    with open('./campus.json', 'r') as f:
        for line in f:
            match = re.findall(r'([A-Za-z0-9]{90,120})', line)

    return match


def get_events_campus(events, url):
    for event in events:
        urllib.request.urlretrieve(url + '/' + event, './temp/' + event[54:] + '.json')


def clean_events_files():
    for files in listdir('./temp/'):
        with open('./temp/' + files, 'r') as fin:
            data = fin.read().splitlines(True)
        with open('./temp/' + files, 'w') as fout:
            fout.writelines(data[1:])


def parser_json_files():
    for files in listdir('./temp/'):
        with open('./temp/' + files, 'r') as f:
            data = json.load(f)

        pprint(data)



events = get_url_campus(url)
get_events_campus(events, url)
clean_events_files()
parser_json_files()
