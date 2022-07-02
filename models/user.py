#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel, represent an User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
