from pymongo import MongoClient

class Database(object):
    DATABASE = None

    @staticmethod
    def initialize():
        client = MongoClient()
        Database.DATABASE = client.posts

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_last(collection):
        return Database.DATABASE[collection].find().sort('_id', -1)
