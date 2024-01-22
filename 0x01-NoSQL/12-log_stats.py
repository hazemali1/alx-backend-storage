#!/usr/bin/env python3
"""pymongo"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    print("    method GET: {}".format(collection.count_documents({"method": "GET"})))
    print("    method POST: {}".format(collection.count_documents({"method": "POST"})))
    print("    method PUT: {}".format(collection.count_documents({"method": "PUT"})))
    print("    method PATCH: {}".format(collection.count_documents({"method": "PATCH"})))
    print("    method DELETE: {}".format(collection.count_documents({"method": "DELETE"})))
    print("{} status check".format(collection.count_documents({"method": "GET", "path": "/status"})))
