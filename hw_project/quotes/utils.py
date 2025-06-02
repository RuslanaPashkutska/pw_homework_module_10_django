from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")

    db = client.hw
    return db
