from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

data = [
    {
        "id": 1,
        "name": "Michael Scott",
        "seasons": "7"
    },
    {
        "id": 2,
        "name": "Jim Halpert",
        "seasons": "9"
    },
    {
        "id": 3,
        "name": "Dwight Schrute",
        "seasons": "9"
    }
]


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(data), 200
        for quote in data:
            if (quote["id"] == id):
                return quote, 200
        return "Quote not found", 404


api.add_resource(Quote, "/data", "/data/", "/data/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)