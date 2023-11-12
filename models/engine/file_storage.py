"""module for engine store."""

class FileStorage:
    """class for serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dict"""
        return __objects

    def new(self, obj):
        """set in __objects"""
        k = str(self.__class__.name)
        k += self.id
        __objects.append({k: self.__dict__})
