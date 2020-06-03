#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# index
@app.route('/')
def homeindex():
    return "Welcome to my Movies API"

@app.route("/movies/")
def movies():
    try:
        qparms = {}
        # user passes switchname= or default "bootstrapped switch"
        qparms["moviename"] = request.args.get("moviename", "Scarface")
        # user passes username= or default "admin"
        qparms["rating"] = int(request.args.get("rating", "1"))
        # user passes gateway= or default "0.0.0.0"
        qparms["reviewer"] = request.args.get("reviewer", "John Doe")
        # user passes ip= or default "0.0.0.0"
        qparms["comments"] = request.args.get("comments", "Default Comment")
        # render template and save as baseIOS.conf
        return render_template("movies.conf.j2", **qparms)

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
