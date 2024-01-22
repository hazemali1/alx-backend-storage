#!/usr/bin/env python3
"""pymongo"""


def top_students(mongo_collection):
    """top students"""
    obj = [
        {
    "$addFields": {
      "averageScore": { "$avg": "$topics.score" }
    }
  },
  {
    "$project": {
      "name": 1,
      "averageScore": 1
    }
  },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(obj))
