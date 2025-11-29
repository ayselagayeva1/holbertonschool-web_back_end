#!/usr/bin/env python3
"""
9-insert_school.py
Insert a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection: pymongo collection object
    **kwargs: key/value pairs to insert as document
    Returns: the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
