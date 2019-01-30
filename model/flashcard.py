"""Represent the data model for a flashcard."""
import uuid
import json


class Flashcard:
    """Represent a flashcard with related fields and methods."""

    def __init__(self, question, answer, group_id, creator_id):
        """Create a flashcard."""
        self.__flashcard_id = uuid.uuid4().int
        self.__question = question
        self.__answer = answer
        self.__group_id = group_id
        self.__creator_id = creator_id

    def __str__(self):
        """Return stringified dictionary of this flashcard."""
        flashcard_dict = {
            "flashcard_id": self.__flashcard_id,
            "question": self.__question,
            "answer": self.__answer,
            "group_id": self.__group_id,
            "creator_id": self.__creator_id
        }
        return json.dumps(flashcard_dict)

    def get_flashcard_id(self):
        """Get this flashcard's id."""
        return self.__flashcard_id

    def get_question(self):
        """Get this flashcard's question."""
        return self.__question

    def set_question(self, question):
        """Set this flashcard's question."""
        self.__question = question

    def get_answer(self):
        """Get this flashcard's answer."""
        return self.__answer

    def set_answer(self, answer):
        """Set this flashcard's answer."""
        self.__answer = answer

    def get_group_id(self):
        """Get this flashcard's associated group id."""
        return self.__group_id

    def get_creator_id(self):
        """Return the user id of the creator of this flashcard."""
        return self.__creator_id
