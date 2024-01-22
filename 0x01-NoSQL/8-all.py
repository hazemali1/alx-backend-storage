#!/usr/bin/env python3
"""pymongo"""


def list_all(mongo_collection):
    """list all"""
    mongo_collection.find()
