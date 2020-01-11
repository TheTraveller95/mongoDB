import pymongo
import os

os.environ["MONGO_URI"] = "mongodb+srv://root:<PASSWORD>@myfirstcluster-p7dea.mongodb.net/TEST?retryWrites=true&w=majority" # add the db password insead of <PASSWORD> and the db name instead of TEST
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):

    try:
        conn = pymongo.MongoClient(url)
        return conn

    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB:%s') % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_doc = {'first':'douglas', 'last':'adams', 'dob':'11/03/1952', 'hair_colour':'grey', 'occupation':'writer', 'nationality':'english'} after having inserted it we need to delete it

#coll.insert(new_doc)

# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender':'m', 'hair_colour':'not much', 'occupation':'writer', 'nationality':'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender':'m', 'hair_colour':'white', 'occupation':'writer', 'nationality':'american'}]

# coll.insert_many(new_docs)

#coll.remove({'first':'douglas'})

#coll.update_many({'nationality':'american'}, {'$set':{'hair_colout':'maroon'}})

documents = coll.find()

for doc in documents:
    print(doc)
