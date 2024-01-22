#!/usr/bin/env python3
"""pymongo"""


def insert_school(mongo_collection, **kwargs):
    """insert"""
    obj = {}
    for key, value in kwargs.items():
        obj[key] = value
    return mongo_collection.insert_one(obj).inserted_id
