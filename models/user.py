#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The user's email.
        password (str): user's password.
        first_name (str): first name.
        last_name (str): and the last name of the user.
    """

    email = " "
    password = " "
    first_name = " "
    last_name = " "
