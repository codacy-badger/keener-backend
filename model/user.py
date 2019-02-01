"""Represent the data model for a user."""
import json


class User:
    """Represent a user with related fields and methods."""

    def __init__(self, sub, email, name, given_name, picture_url):
        """Create a user with Google sign-in information."""
        self.__user_id = sub
        self.__email = email
        self.__name = name
        self.__given_name = given_name
        self.__picture_url = picture_url
        self.__flashcard_ids = []

    def __str__(self):
        """Return a stringified dictionary of this user."""
        user_dict = {
            "user_id": self.__user_id,
            "email": self.__email,
            "name": self.__name,
            "given_name": self.__given_name,
            "picture_url": self.__picture_url,
            "flashcard_ids": self.__flashcard_ids
        }
        return json.dumps(user_dict)

    def get_user_id(self):
        """Get this user's id."""
        return self.__user_id

    def get_email(self):
        """Get this user's email."""
        return self.__email

    def set_email(self, email):
        """Set this user's email."""
        self.__email = email

    def get_name(self):
        """Get this user's name."""
        return self.__name

    def set_name(self, name):
        """Set this user's name."""
        self.__name = name

    def get_given_name(self):
        """Get this user's given name."""
        return self.__name

    def set_given_name(self, given_name):
        """Set this user's given name."""
        self.__given_name = given_name

    def get_picture_url(self):
        """Get this user's picture url."""
        return self.__picture_url

    def set_picture_url(self, picture_url):
        """Set this user's picture url."""
        self.__picture_url = picture_url

    def get_flashcard_ids(self):
        """Get this user's list of flashcard ids."""
        return self.__flashcard_ids

    def add_flashcard_id(self, flashcard_id):
        """Add a flashcard to the user via its id."""
        self.flashcard_ids.append(flashcard_id)

    def delete_flashcard_id(self, flashcard_id):
        """
        Delete a flashcard from the user via its id.

        Return non-zero if flashcard id was not present.
        """
        if flashcard_id in self.__flashcard_ids:
            self.__flashcard_ids.remove(flashcard_id)
            return 0
        else:
            return 1
