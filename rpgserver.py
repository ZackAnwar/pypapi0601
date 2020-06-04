#!/usr/bin/python3
"""Welcome to Alta3 Web RPG"""

import json
from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

"""
Flask Sessions are leveraged to store encrypted cookie data, the player's state, on the client side.

API endpoints:

   /new/ - start a new game
   
   /status/ - return the current status of the player

   /go/<direction> - attempt to move in a direction

   /get/<item> - attempt to pick up an item

   /help/ - return help

   /look/ - return what is in the room, an abbreviated form of /status/
"""


# create the world object
with open ("world.json", "r") as world:
    rooms = json.load(world)


app = Flask(__name__)
app.secret_key = "rzfeeser:RAND"
