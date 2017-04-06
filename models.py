from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    title = Column(String(30))
    description = Column(String(200))   

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return json.dumps(self.serialize, indent=4)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {u"id": self.id,
                u"title": self.title,
                u"description": self.description}