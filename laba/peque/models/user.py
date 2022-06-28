#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel, represent an User"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
