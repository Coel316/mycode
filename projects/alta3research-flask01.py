#!/usr/bin/env python3
"""App with JSON"""

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import jsonify
from flask import render_template

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

@app.route('/getcookie', methods=["GET","POST"])
def cookiename():
    cookievalue = request.cookies.get('my_cookie_name')
    if cookievalue == None:
       cookievalue = "cookie exists, but will not display in terminal"
    
    return cookievalue

@app.route('/setcookie', methods=["GET","POST"])
def setcookiename():
    response = make_response("<h1>cookie is set</h1>")
    response.set_cookie('my_cookie_name', "cookie duplicator")

    return response 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
