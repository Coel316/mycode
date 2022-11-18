#!/usr/bin/env python3
"""App with JSON"""

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import jsonify

import json

app= Flask(__name__)

realchar = [{
    "name": "John-the-Revelator",
    "realName": "John",
    "since": 11,
    "powers": [
        "Obedience",
        "Revealer of truth",
        "Insight into the future",
        "unstoppable for Christ",
        "Survived burning oil"
              ]
             }]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           realName = data["realName"]
           since = data["since"]
           powers = data["powers"]
           realchar.append({"name":name,"realName":realName,"since":since,"powers":powers})

    return jsonify(realchar)

# takes a cookie name
@app.route('/getcookie')
def cookiename():
    # checks to see if there is a cookie calld my_cookie_name
    # 1st time this is called, it wil retrun nothing
    #2nd time it's called, it will return a set cookie
    username = request.cookies.get('my_cookie_name')
    if username == None:
        username = "no cookie"
    response = make_response("<h1>cookie is set</h1>" + username)
    # when called, cookie was already set, and will display super-human
    response.set_cookie('my_cookie_name', 'super-human')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

