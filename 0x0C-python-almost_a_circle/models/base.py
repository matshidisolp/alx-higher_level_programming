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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a JSON file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            try:
                if list_objs is None:
                    file.write("[]")
                else:
                    list_dicts = [obj.to_dictionary() for obj in list_objs]
                    file.write(cls.to_json_string(list_dicts))
            except Exception as e:
                print(f"Error saving to file: {e}")

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        # Creating a dummy instance with mandatory attributes
        dummy_instance = cls(1)  # Assuming 1 as a dummy value for id

        # Updating the dummy instance with the provided dictionary
        dummy_instance.update(**dictionary)

        return dummy_instance

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries from a JSON string"""

        if not json_string or json_string == "[]":
            return []

        return json.loads(json_string)

# Example usage:
# json_string = '[{"id": 89, "width": 10, "height": 4},
# {"id": 7, "width": 1, "height": 7}]'
# list_output = Base.from_json_string(json_string)
