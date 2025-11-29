#!/usr/bin/env python3
"""
8-all.py
List all documents in a collection
"""

def list_all(mongo_collection):
    """
    mongo_collection: pymongo collection object
    Returns: list of all documents in the collection
             empty list if none
    """
    return list(mongo_collection.find({}))
