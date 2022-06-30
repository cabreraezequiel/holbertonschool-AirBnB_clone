#!/usr/bin/python3
""" Class definition """
import datetime
import uuid
from models import storage


class BaseModel:
    """ Class BaseModel """
    def __init__(self, *args, **kwargs):
        """ intialize instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs is not None and kwargs is not {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        if len(kwargs) == 0 or kwargs is None:
            storage.new(self)

    def __str__(self):
        """ overrides str method """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        of the instance """
        dic = self.__dict__
        dic["created_at"] = (self.__dict__["created_at"]).isoformat()
        dic["updated_at"] = (self.__dict__["updated_at"]).isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic
