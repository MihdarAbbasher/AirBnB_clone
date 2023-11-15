""" defines all common attributes/methods for other classes """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base class for other class to inherit from it"""

    def __init__(self, *args, **kwargs):
        """ Initialize instantce obj"""
        if len(kwargs) > 0:
            for k in kwargs:
                v = kwargs[k]
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                elif k == "__class__":
                    continue
                setattr(self, k, v)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """overwrite str method"""
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return (s)

    def save(self):
        """ Save changes and update time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return key: value of instance __dict__ """
        myDic = {**self.__dict__}
        myDic['created_at'] = str(self.created_at.isoformat())
        myDic['updated_at'] = str(self.updated_at.isoformat())
        myDic['__class__'] = type(self).__name__
        return myDic
