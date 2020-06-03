#!/usr/bin/python3
from flask import Flask
from flask import request

with open("inseason.txt") as f:
    insea = f.readlines()
    insea = set(insea)
    print(insea)

app = Flask(__name__)

# when the user lands at the "root" (/)
# this should return text about services available
@app.route("/")
def zindex():
    return "Seasonal information is available at /inseason"

# when the user lands at "inseason" (/inseason)
# the query param "fruit" is expected
# if it is not supplied, send by an error message
# if the value associated with "fruit" does not exist
# send back "I am sorry we do not carry that item."
@app.route("/inseason")
def inseason():
    if request.args.get("fruit"):
        fruitq = request.args.get("fruit")
    else:
        return "To use this endpoint, you need to pass the query param 'fruit'"

    if fruitq+"\n" in insea:
        return f"Yes, {fruitq} are in season"
    else:
        return "I'm sorry, that item is not in season"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
