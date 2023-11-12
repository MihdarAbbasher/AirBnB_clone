""" defines all common attributes/methods for other classes """
import uuid
from datetime import datetime


class BaseModel:
    """ Base class for other class to inherit from it"""

    def __init__(self):
        """ Initialize instantce obj"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """overwrite str method"""
        s = "[" + type(self).__name__ + "] (" + self.id + ") "
        s += str(self.__dict__)
        print(s)
        return(s)

    def save(self):
        """ Save changes and update time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return key: value of instance __dict__ """
        self.created_at = str(self.created_at.isoformat())
        return self.__dict__
