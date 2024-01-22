#!/usr/bin/env python3
"""pymongo"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
