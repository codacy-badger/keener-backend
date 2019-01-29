"""Test the flashcard data model."""
import pytest
from model.flashcard import Flashcard


@pytest.fixture
def flashcard():
    """Return an instance of a flashcard."""
    return Flashcard("question", "answer", 0, 0)


def test_get_flashcard_id(flashcard):
    """Test get_flashcard_id()."""
    assert isinstance(flashcard.get_flashcard_id(), int)


def test_get_question(flashcard):
    """Test get_question()."""
    assert flashcard.get_question() is "question"


def test_set_question(flashcard):
    """Test set_question()."""
    flashcard.set_question("another question")
    assert flashcard.get_question() is "another question"


def test_get_answer(flashcard):
    """Test get_answer()."""
    assert flashcard.get_answer() is "answer"


def test_set_answer(flashcard):
    """Test set_answer()."""
    flashcard.set_answer("another answer")
    assert flashcard.get_answer() is "another answer"


def test_get_group_id(flashcard):
    """Test get_group_id()."""
    assert flashcard.get_group_id() is 0


def test_get_creator_id(flashcard):
    """Test get_creator_id()."""
    assert flashcard.get_creator_id() is 0
