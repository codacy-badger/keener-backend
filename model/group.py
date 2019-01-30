"""Represent the data model for a study group."""
import uuid
import json


class Group:
    """Represent a study group with related fields and methods."""

    def __init__(self, group_name):
        """Create a study group."""
        self.__group_id = uuid.uuid4().int
        self.__group_name = group_name
        self.__member_ids = []
        self.__flashcard_ids = []

    def __str__(self):
        """Return stringified dictionary of this group."""
        group_dict = {
            "group_id": self.__group_id,
            "group_name": self.__group_name,
            "member_ids": {},
            "flashcard_ids": {}
        }
        return json.dumps(group_dict)

    def get_group_id(self):
        """Get this group's id."""
        return self.__group_id

    def get_group_name(self):
        """Get this group's name."""
        return self.__group_name

    def set_group_name(self, group_name):
        """Set this group's name."""
        self.__group_name = group_name

    def get_member_ids(self):
        """Get this group's list of member ids."""
        return self.__member_ids

    def add_member_id(self, member_id):
        """Add a member to the group via their id."""
        self.__member_ids.append(member_id)

    def delete_member_id(self, member_id):
        """
        Delete a member from the group via their id.

        Return non-zero if member id was not present.
        """
        if member_id in self.__member_ids:
            self.__member_ids.remove(member_id)
            return 0
        else:
            return 1

    def get_flashcard_ids(self):
        """Get this group's list of flashcard ids."""
        return self.__flashcard_ids

    def add_flashcard_id(self, flashcard_id):
        """Add a flashcard to the group via its id."""
        self.__flashcard_ids.append(flashcard_id)

    def delete_flashcard_id(self, flashcard_id):
        """
        Delete a flashcard from the group via its id.

        Return non-zero if flashcard id was not present.
        """
        if flashcard_id in self.__flashcard_ids:
            self.__flashcard_ids.remove(flashcard_id)
            return 0
        else:
            return 1
