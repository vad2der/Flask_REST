from models import Item, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from datetime import datetime

# db config
engine = create_engine('sqlite:///items.db')
session = sessionmaker()
session.configure(bind=engine)
s = session()

def create_tables():
    # table drop and creation
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    #print "table created"


def get_all():
    # get all entries
    #print "requesting all entries"
    return s.query(Item).order_by(Item.title).all()

def get_by_title(title):
    # get all entries
    return s.query(Item).filter(Item.title.like('%'+str(title)+'%')).order_by(Item.title).all()

def get_by_id(id):
    # get the entry
    return s.query(Item).filter(Item.id == id).first()

def insert_new(title, description):    
    # instantiate a new object from mapped class
    item = Item(title=str(title), description=str(description))
    #print rt
    try:
        s.add(item)
        s.commit()
        #print "ok"
    except Exception as e:
        s.rollback()

def delete_entry(id):
    #print "ID to Delete is: {}".format(str(id))
    s.query(Item).filter(Item.id == id).delete()

def update_entry(item):
    item = {'id': item['id'],
          'title': item['title'],
          'description': item['description']}
    s.query(Item).filter(Item.id == item['id']).update(item)

def seed():
    elements = [{'title':"Title {0}".format(str(i)), 'description':"Description for Title {0}".format(str(i))} for i in range(5)]
    for el in elements:
        insert_new(el['title'], el['description'])
    #print "seeding done"