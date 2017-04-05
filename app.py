from flask import Flask, request, Request, render_template
from flask_restful import Api, Resource, fields, marshal_with
import requests
import json

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
                "title": fields.String,
                "gm_url": fields.String}


class Item_api(Resource):
    """
    class for API
    """
    @marshal_with(output_fields)
    def get(self, param):
        if param == "all":
            output1 = requests.get("https://item-api.herokuapp.com/api/v1/items").text
            output2 = json.loads(output1)
            for o in output2:
                o["gm_url"] = "https://www.google.ca/maps/place/{0} {1}".format(str(o["seller_latitude"]), str(o["seller_longitude"]))
            return output2, 200

    def post(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

api.add_resource(Item_api, '/api/v1/item/<param>')

if __name__ == "__main__":    
    app.run(port=5000, debug=True)