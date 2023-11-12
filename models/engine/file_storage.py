"""module for engine store."""

import json
import os

class FileStorage:
    """class for serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dict"""
        return __objects

    def new(self, obj):
        """set in __objects"""
        k = "{}.{}".format(type(self).__name__, self.id)
        __objects[k] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as myfile:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, myfile)

    def reload(self):
        """
        deserializes the JSON file to __objects dict, if the JSON file is exist"""
        my_classes = {'BaseModel': BaseModel}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                deserialized = None

                try:
                    deserialized = json.load(f)
                except json.JSONDecodeError:
                    pass

                if deserialized is None:
                    return

                __objects = {
                    k: my_classes[k.split('.')[0]](**v)
                    for k, v in deserialized.items()}
