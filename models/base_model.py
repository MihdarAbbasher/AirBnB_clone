""" defines all common attributes/methods for other classes """
import uuid


class BaseModel:
    """ Base class for other class to inherit from it"""

    def __init__():
        """ Initialize instantce obj"""
        self.id = uuid.uuid4()
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """overwrite str method"""
        print(self.className, " (", self.id, ") ", self.__dict__)

    def save(self):
        """ Save changes and update time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return key: value of instance __dict__ """
        self.__dict__.__class__ = self.className
        self.created_at = str(self.created_at.isoformat())
        return self.__dict__
