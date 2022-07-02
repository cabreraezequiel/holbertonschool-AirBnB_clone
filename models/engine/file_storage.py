#!/usr/bin/python3
""" Class definition """
import json


class FileStorage:
    """ Serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    @staticmethod
    def classes():
        """All available classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.state import State

        class_dict = {'BaseModel' : BaseModel , 'User' : User, 'Place': Place,
                      'City': City, 'Amenity': Amenity, 'Review': Review,
                      'State': State}
        return class_dict

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        to_dicted = self.__objects.copy()
        for k, v in to_dicted.items():
            to_dicted[k] = v.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(to_dicted, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.loads(f.read())
                class_dict = self.classes()
                for k, v in data.items():
                    new_instance = class_dict[(k.split('.')[0])](**v)
                    self.__objects[k] = new_instance
        except Exception:
            pass
