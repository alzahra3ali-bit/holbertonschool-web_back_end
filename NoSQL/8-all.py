#!/usr/bin/env python3
"""
Module that contains a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a Python pymongo collection.
    Returns an empty list if no document in the collection.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())