import db_layer as db
from flask import Flask, request, Request, render_template
from flask_restful import Api, Resource, fields, marshal_with
import requests
import json


app = Flask(__name__)
api = Api(app)

output_fields = {"id": fields.Integer,
                "title": fields.String,
                "description": fields.String}


class Item_api(Resource):
    """
    class for API
    """
    @marshal_with(output_fields)
    def get(self, param):
        if param=="all":
            return db.get_all(), 200
        elif param=="title":
            title = request.args.get('title')            
            return db.get_by_title(title)
        elif param.isdigit():
            id = int(param)
            print id
            return db.get_by_id(id)
        else:
            return ""

    def post(self):
        return db.insert_new(title=request.form.get('title'),
                             description=request.form.get('description')), 201

    def delete(self):
        delete_entry(id=request.form.get('id'))
        return '', 204

    def update(self):
        update_entry(id=request.form.get('id'),
                     title=request.form.get('title'),
                     description=request.form.get('description'))
        return '', 201

api.add_resource(Item_api, '/api/v1/item/<param>')

if __name__ == "__main__":
    db.create_tables()
    db.seed()
    app.run(port=5000, debug=True)