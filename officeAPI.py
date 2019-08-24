from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import random, os

data = [
    {
        "id": 1,
        "name": "Michael Scott",
        "realname": "Steve Carell",
        "seasons": "1-7"
    },
    {
        "id": 2,
        "name": "Jim Halpert",
        "realname": "John Krasinski",
        "seasons": "1-9"
    },
    {
        "id": 3,
        "name": "Dwight K. Schrute",
        "realname": "Rainn Wilson",
        "seasons": "1-9"
    },
    {
        "id": 4,
        "name": "Toby",
        "realname": "Paul Lieberstein",
        "seasons": "1-9"
    },
    {
        "id": 5,
        "name": "Pam Beesly",
        "realname": "Jenna Fischer",
        "seasons": "1-9"
    },
    {
        "id": 6,
        "name": "Ryan Howard",
        "realname": "B.J. Novak",
        "seasons": "1-9"
    },
    {
        "id": 7,
        "name": "Andy Bernard",
        "realname": "Ed Helms",
        "seasons": "3-9"
    },
    {
        "id": 8,
        "name": "Robert California",
        "realname": "James Spader",
        "seasons": "7-8"
    },
    {
        "id": 9,
        "name": "Angela Martin",
        "realname": "Angela Kinsey",
        "seasons": "1-9"
    },
    {
        "id": 10,
        "name": "Stanley Hudson",
        "realname": "Leslie David Baker",
        "seasons": "1-9"
    },
    {
        "id": 11,
        "name": "Kevin Malone",
        "realname": "Brian Baumgartner",
        "seasons": "1-9"
    },
    {
        "id": 12,
        "name": "Creed Bratton",
        "realname": "Creed Bratton",
        "seasons": "1-9"
    },
    {
        "id": 13,
        "name": "Meredith Palmer",
        "realname": "Kate Flannery",
        "seasons": "1-9"
    },
    {
        "id": 14,
        "name": "Kelly Kapoor",
        "realname": "Mindy Kaling",
        "seasons": "1-9"
    },
    {
        "id": 15,
        "name": "Erin Hannon",
        "realname": "Ellie Kemper",
        "seasons": "5-9"
    },
    {
        "id": 16,
        "name": "Oscar Martinez",
        "realname": "Oscar Nunez",
        "seasons": "1-9"
    },
    {
        "id": 17,
        "name": "Darryl Philbin",
        "realname": "Craig Robinson",
        "seasons": "1-9"
    },
    {
        "id": 18,
        "name": "Phyllis Lapin",
        "realname": "Phyllis Smith",
        "seasons": "1-9"
    },
    {
        "id": 19,
        "name": "Gabe Lewis",
        "realname": "Zach Woods",
        "seasons": "6-8"
    },
    {
        "id": 20,
        "name": "Holly Flax",
        "realname": "Amy Ryan",
        "seasons": "4-7"
    },
    {
        "id": 21,
        "name": "Karen Filippelli",
        "realname": "Rashida Jones",
        "seasons": "3-7"
    },
    {
        "id": 22,
        "name": "Jan Levenson",
        "realname": "Melora Hardin",
        "seasons": "1-5,7"
    },
    {
        "id": 23,
        "name": "Roy Anderson",
        "realname": "David Denman",
        "seasons": "1-3"
    },
    {
        "id": 24,
        "name": "Nellie Bertram",
        "realname": "Catherine Tate",
        "seasons": "7-9"
    },
    {
        "id": 25,
        "name": "David Wallace",
        "realname": "Andy Buckley",
        "seasons": "1-9"
    },
    {
        "id": 26,
        "name": "Bob Vance",
        "realname": "Bobby Ray Shafer",
        "seasons": "2-9"
    }
]

app = Flask(__name__)

api = Api(app)

picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder


@app.route("/")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'mike.jpg')
    return render_template("index.html", user_image=full_filename)


'''@app.route("/")
def index():
    return "Hi welcome to The Office API beta, try adding /data/1 to the url.. full documentation coming soon.." \
           "" \
           "" \
           "" \
           "" \
           "With Love from Lakshya Srivastava <3 :D"'''


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(data), 200
        for quote in data:
            if (quote["id"] == id):
                return quote, 200
        return "Really bro!, try 26 it's last", 404


api.add_resource(Quote, "/data", "/data/", "/data/<int:id>")
if __name__ == '__main__':
    app.run(debug=False)
