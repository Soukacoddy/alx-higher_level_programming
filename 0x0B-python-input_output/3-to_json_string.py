#!/usr/bin/python3
"""Defines a function that returns a json string"""
import json


def to_json_string(my_obj):
    """
    JSON representation of an object

    Args:
        my_obj (str): the object used
    Returns:
        the json representation
    """
    return json.dumps(my_obj)
