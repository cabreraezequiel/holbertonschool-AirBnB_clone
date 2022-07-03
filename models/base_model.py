#!/usr/bin/python3
""" Class definition """
import datetime
import uuid
from models import storage


class BaseModel:
    """ Class BaseModel """
    def __init__(self, *args, **kwargs):
        """ intialize instance """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    value = datetime.datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ overrides str method """
        print_dic = {k: self.__dict__[k] for k in self.__dict__ if k !=
                     '__class__'}
        return(f"[{self.__class__.__name__}] ({self.id}) {print_dic}")

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        of the instance """
        dic = {key: value for key, value in self.__dict__.items()}
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic
