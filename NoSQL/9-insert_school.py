#!/usr/bin/env python3
"""Module that inserts a document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: fields of the new document.

    Returns:
        The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
