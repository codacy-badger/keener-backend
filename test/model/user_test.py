"""Test the user data model."""
import pytest
import json
from model.user import User


@pytest.fixture
def user():
    """Return an instance of a user."""
    return User("000", "ex@ample.com", "John Doe", "John", "some url")


def test_stringify(user):
    """Test __str__()."""
    user_dict = json.loads(user.__str__())
    assert user_dict.get("user_id") is not None
    assert user_dict.get("email") is not None
    assert user_dict.get("name") is not None
    assert user_dict.get("given_name") is not None
    assert user_dict.get("picture_url") is not None
    assert user_dict.get("flashcard_ids") is not None


def test_get_user_id(user):
    """Test get_user_id()."""
    assert user.get_user_id() == "000"


def test_get_email(user):
    """Test get_email()."""
    assert user.get_email() == "ex@ample.com"


def test_set_email(user):
    """Test set_email()."""
    user.set_email("johndoe@ample.com")
    assert user.get_email() == "johndoe@ample.com"


def test_get_name(user):
    """Test get_name()."""
    assert user.get_name() == "John Doe"


def test_set_name(user):
    """Test set_name()."""
    user.set_name("Some Name")
    assert user.get_name() == "Some Name"


def test_get_given_name(user):
    """Test get_given_name()."""
    assert user.get_given_name() == "John"


def test_set_given_name(user):
    """Test set_given_name()."""
    user.set_given_name("Some")
    assert user.get_given_name() == "Some"


def test_get_picture_url(user):
    """Test get_picture_url()."""
    assert user.get_picture_url() == "some url"


def test_set_picture_url(user):
    """Test set_picture_url()."""
    user.set_picture_url("other url")
    assert user.get_picture_url() == "other url"


def test_get_flashcard_ids(user):
    """Test get_flashcard_ids()."""
    assert user.get_flashcard_ids() == []


def test_add_flashcard_id(user):
    """Test add_flashcard_id()."""
    user.add_flashcard_id(0)
    assert 0 in user.get_flashcard_ids()


def test_delete_flashcard_id(user):
    """Test delete_flashcard_id()."""
    assert user.delete_flashcard_id(0)
    user.add_flashcard_id(0)
    assert not user.delete_flashcard_id(0)
