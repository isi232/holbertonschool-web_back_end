#!/usr/bin/env python3
"""Module that lists all documents in a collection."""


def list_all(mongo_collection):
    """Return a list of all documents in the collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents, or an empty list if there are none.
    """
    return list(mongo_collection.find())
