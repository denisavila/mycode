#!/usr/bin/env python3

import requests

response = requests.get('https://frederick.craigslist.org/d/free-stuff/search/zip')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

print(response.headers)
