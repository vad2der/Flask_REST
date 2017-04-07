import db_layer as db
from flask import Flask, request, Request, render_template
from flask_restful import Api, Resource, fields, marshal_with
from flask_cache import Cache
import requests
import json


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
api = Api(app)

output_fields = {"id": fields.Integer,
                "title": fields.String,
                "description": fields.String}


class Item_api(Resource):
    """
    class for API
    """
    #@cache.cached(timeout=50, key_prefix='items')
    #@cache.memoize(timeout=50)
    @marshal_with(output_fields)
    def get(self, param):
        if param=="all":
            return self.get_all()
        elif param=="title":
            title = request.args.get('title')            
            return self.get_by_title(title)
        elif param.isdigit():
            id = int(param)
            return self.get_by_id(id)
        else:
            return ""
    
    @cache.cached(timeout=50, key_prefix='all_items')
    def get_all(self):
        return db.get_all(), 200
    
    def get_by_title(self, title):
        return db.get_by_title(title)

    def get_by_id(self, id):
        return db.get_by_id(id)

    def post(self, param):
        if param == 'new':
            db.insert_new(title=request.form.get('title'),
                          description=request.form.get('description'))
            cache.clear()
            return '', 201

    def delete(self, param):
        if param == "delete":
            id=request.form.get('id')
            db.delete_entry(id)
            cache.clear()
            return '', 204

    def put(self, param):
        if param == "update":
            db.update_entry({'id':request.form.get('id'),
                             'title':request.form.get('title'),
                             'description':request.form.get('description')})
            cache.clear()
        return '', 201

api.add_resource(Item_api, '/api/v1/item/<param>')

if __name__ == "__main__":
    db.create_tables()
    db.seed()
    app.run(port=5000, debug=True)