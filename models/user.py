#!/usr/bin/python3
<<<<<<< HEAD
"""User class"""
=======
"""Defines the User class."""
>>>>>>> a2667300aff346dc5092b189dcc5c7396bd5fceb
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """User class"""
=======
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

>>>>>>> a2667300aff346dc5092b189dcc5c7396bd5fceb
    email = ""
    password = ""
    first_name = ""
    last_name = ""
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        """initialise class"""
        super().__init__(*args, **kwargs)
=======
>>>>>>> a2667300aff346dc5092b189dcc5c7396bd5fceb
