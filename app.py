from flask import Flask, request, Request, render_template
from flask_restful import Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

output_fields = {"field1": fields.Integer,
                "field2": fields.Float,
                "field3": fields.Float}


class Item_api(Resource):
    """
    class for API
    """
    @marshal_with(output_fields)
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

api.add_resource(Item_api, '/api/v1/item/')

if __name__ == "__main__":    
    app.run(port=5000, debug=True)