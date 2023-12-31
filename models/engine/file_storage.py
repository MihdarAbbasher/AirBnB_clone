"""module for engine store."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """class for serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dict"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj
        self.save()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as myfile:
            values = FileStorage.__objects.items()
            json.dump({k: v.to_dict() for k, v in values}, myfile)

    def reload(self):
        """
        deserializes the JSON file to __objects dict,
        if the JSON file is exist"""
        my_classes = {"BaseModel": BaseModel, "User": User, "City": City, "State": State, "Place": Place, "Review": Review,
    "Amenity": Amenity}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                deserialized = None

                try:
                    deserialized = json.load(f)
                except json.JSONDecodeError:
                    pass

                if deserialized is None:
                    return

                FileStorage.__objects = {
                    k: my_classes[k.split('.')[0]](**v)
                    for k, v in deserialized.items()}
