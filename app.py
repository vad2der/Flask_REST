from flask import Flask, request, Request, render_template
from flask_restful import Api, Resource, fields, marshal_with
import requests
import json

app = Flask(__name__)
api = Api(app)


class Item_api(Resource):
    """
    class for API
    """
    def get(self, param):
        pass
        
    def post(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

api.add_resource(Item_api, '/api/v1/item/<param>')

if __name__ == "__main__":    
    app.run(port=5000, debug=True)