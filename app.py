from flask import Flask, request, Request, render_template
from flask_restful import Api, Resource, fields, marshal_with
import requests
import simplejson

app = Flask(__name__)
api = Api(app)

output_fields = {"id": fields.Integer,
                "description": fields.String,
                "price": fields.Float,
                "published_date": fields.String,
                "seller_latitude": fields.Float,
                "seller_longitude": fields.Float,
                "seller_name": fields.String,
                "status": fields.String,
                "title": fields.String}


class Item_api(Resource):
    """
    class for API
    """
    @marshal_with(output_fields)
    def get(self, param):
        if param == "all":
            output = requests.get("https://item-api.herokuapp.com/api/v1/items").text
            output = simplejson.load(ouptut)
            return output, 200

    def post(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

api.add_resource(Item_api, '/api/v1/item/<param>')

if __name__ == "__main__":    
    app.run(port=5000, debug=True)