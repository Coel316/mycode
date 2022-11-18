#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

new_realchar= {
           "name": "Christ",
           "realName": "Jesus Christ",
           "since": 1,
           "powers": [
                "heal the sick",
                "give sight to blind",
                "heal the leper",
                "calm the sea"]
               }

# json.dumps takes a python object and returns it as a JSON string
new_realchar= json.dumps(new_realchar)

# requests.post requires two arguments - a URL (for request)
# and a json string to attach to the request
resp = requests.post(URL, json = new_realchar)

# pretty-print the response back from our POST request
pprint(resp.json())

# append 'getcookie' and 'setcookie'
res2 = requests.get(URL + "setcookie")
res3 = requests.get(URL + "getcookie")

# print the results
print(res2.text)
print(res3.text)
