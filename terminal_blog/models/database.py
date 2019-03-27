from pymongo import MongoClient

class Database(object):
    DATABASE = None

    @staticmethod
    def initialize():
        client = MongoClient()
        Database.DATABASE = client.fullstack

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
