from kafka import KafkaConsumer
from pymongo import MongoClient

# MongoDB connection
import pymongo
import os
from urllib.parse import quote_plus
import ssl

class MongoDB():
    def __init__(self, url=None, ) -> None:
        # Connect to Mongo only once
        if url is None:
            self.url = os.environ['MONGO_URL']
        else:
            self.url = url
        # configure the PyMongo client to use the more modern, cross-language compatible "standard" UUID representation
        self.client = pymongo.MongoClient(self.url, uuidRepresentation="standard") 
        

    def get_doc(self, db, collection, query=None):
        """Get specific document from a collection found by query
        Args:
            db (str): Database name
            col (str): Collection name
            query (dict): Query for one entry in the database on col
        Returns:
            doc (dict): Document found otherwise None
        """
        db = self.client[db]
        col = db[collection]
        doc = col.find_one(query)
        return doc


    def insert_doc(self, db, collection, new_doc):
        """Inserts a new document into a MongoDB collection.
        Args:
            db (str): The name of the MongoDB database to use.
            collection (str): The name of the collection within the database.
            new_doc(dict): A dictionary representing the new document to insert.

        Returns:
            The ID of the inserted document.
        """
        db = self.client[db]
        col = db[collection]
        result = col.insert_one(new_doc)
        return result.inserted_id


    def update_doc(self, db, collection, filter, new_doc, upsert=True):
        """Updates a single document in a MongoDB collection.
        Args:
            db (str):The name of the MongoDB database to use.
            collection (str): The name of the collection within the database.
            filter (dict): A dictionary representing the filter to apply to the collection.
            new_doc (dict): The new document that will replace the old one

        Returns:
            The number of documents that were modified by the update operation.
        """
        db = self.client[db]
        col = db[collection]
        filter = filter
        update = {'$set': new_doc}
        result = col.update_one(filter, update, upsert=upsert)
        return result.modified_count


#mongo = MongoDB(f"mongodb+srv://{username}:{password}@iotbigdataproject.courajk.mongodb.net/")
mongo = MongoClient('mongodb://%s:%s@localhost:27017/admin' % ('root', 'root'))
db = mongo['iotbigdataproject']
Temperature_col = db['Temperature']

print("connection to mongo succeeded!")
Temperatureconsumer = KafkaConsumer('Temperature_Topic',auto_offset_reset= "latest",bootstrap_servers= 'localhost:9092')



data={}
for message in Temperatureconsumer :
    message_data = message.value.decode('utf-8')  # Decode message if needed
    # Insert message into MongoDB
    data["Temperature"]=message_data
    Temperature_col.insert_one(data)


