# defines all common attributes/methods for other classes

class BaseModel:
    """ Base class for other class to inherit from it"""

    id = str(uuid.uuid4())
    created_at = datetime.now()
