#!/usr/bin/env python3
"""
Module that contains a function to find schools by a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
    