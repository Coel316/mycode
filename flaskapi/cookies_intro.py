from flask import Flask
from flask import make_response
from flask import request

app = Flask(__name__)
@app.routh("/"
        def home():
        resp = make_response()
        resp.set_cookie("user", "cookie graber")
        return resp

        
@app.route("/cookie")
def eatcookie():
    name = request.cookies.get("user")
    return f'<h1>Welcome {name}</h1>'

if __name__ == "__main__:
    app.run(host = "0.0.0.0", port = 2224)

