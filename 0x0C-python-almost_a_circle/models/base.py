#!/usr/bin/python3
"""Module for Base class"""
import json


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""

        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
