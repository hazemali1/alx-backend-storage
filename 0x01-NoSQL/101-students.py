#!/usr/bin/env python3
"""pymongo"""


def top_students(mongo_collection):
    """top students"""
    return list(mongo_collection.aggregate([{"$group": {"_id": "$name", "averageScore": {"$avg": "$score"}}}, {"$sort": {"averageScore": -1}}]))
