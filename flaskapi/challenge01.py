#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import request

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def seasonald():
   return "seasonal informationdis available at /inseason"

@app.route("/inseason")
def inseason():
    if request.args.get("fruit"):
        fruitq = request.args.get("fruit")
    else:
        return "Pass Parameter fruit"

    if fruitq == "strawberries":
        return"Yes, good fruit"
    elif fruitq == "pumpkins":
        return "no pumkins"
    elif fruitq == "apple"
        return "I Like it"
    else:
        return "no fruit"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODinseasonii
