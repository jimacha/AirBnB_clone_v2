#!/usr/bin/python3
"""
Module: base_model
Contains the BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for other classes to inherit from
    """
    def init(self):
        """
        Initializes a new instance of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def str(self):
        """
        Returns a string representation of the instance
        """
    return "[{}] ({}) {}".format(
        self.class .__name, self.id, self.__dict)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance
        """
        obj_dict = self.dict.copy()
        obj_dict['class'] = self.__class.__name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
    return obj_dict

