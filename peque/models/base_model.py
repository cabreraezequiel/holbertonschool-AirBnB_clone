#!/usr/bin/python3
""" Class definition """
import datetime
import uuid


class BaseModel:
    """ Class BaseModel """
    def __init__(self):
        """ intialize instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ overrides str method """
        return(f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        of the instance """
        new_dict = self.__dict__
        new_dict[__class__] = __class__.__name__
        new_dict[self.created_at] = (new_dict[self.created_at]).isoformat(sep="T")
        return new_dict
