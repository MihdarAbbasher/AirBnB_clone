#!/usr/bin/python3
"""The `review` module.`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of place/house.

    Represents reviews posted by the users
    of the application about a place/house.

    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""
