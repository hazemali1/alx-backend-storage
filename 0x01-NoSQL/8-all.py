#!/usr/bin/env python3
"""pymongo"""


def list_all(mongo_collection):
    """list all"""
    return mongo_collection.find()
