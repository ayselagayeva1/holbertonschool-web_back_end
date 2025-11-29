#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list): list of topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
