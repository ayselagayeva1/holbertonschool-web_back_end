#!/usr/bin/env python3
"""
11-schools_by_topic.py
Return the list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection: pymongo collection object
    topic: string
    Return: list of schools containing topic in their 'topics' field
    """
    return list(mongo_collection.find({"topics": topic}))
