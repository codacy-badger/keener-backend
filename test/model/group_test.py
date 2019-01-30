"""Test the group data model."""
import pytest
import json
from model.group import Group


@pytest.fixture
def group():
    """Return an instance of a group."""
    return Group("group name")


def test_stringify(group):
    """Test __str__()."""
    group_dict = json.loads(group.__str__())
    assert group_dict.get("group_id") is not None
    assert group_dict.get("group_name") is not None
    assert group_dict.get("member_ids") is not None
    assert group_dict.get("flashcard_ids") is not None


def test_get_group_id(group):
    """Test get_group_id()."""
    assert isinstance(group.get_group_id(), int)


def test_get_group_name(group):
    """Test get_group_name()."""
    assert group.get_group_name() == "group name"


def test_set_group_name(group):
    """Test set_group_name()."""
    group.set_group_name("another group name")
    assert group.get_group_name() == "another group name"


def test_get_member_ids(group):
    """Test get_member_ids()."""
    assert group.get_member_ids() == []


def test_add_member_id(group):
    """Test add_member_id()."""
    group.add_member_id(0)
    assert 0 in group.get_member_ids()


def test_delete_member_id(group):
    """Test delete_member_id()."""
    assert group.delete_member_id(0)
    group.add_member_id(0)
    assert not group.delete_member_id(0)


def test_get_flashcard_ids(group):
    """Test get_flashcard_ids()."""
    assert group.get_flashcard_ids() == []


def test_add_flashcard_id(group):
    """Test add_flashcard_id()."""
    group.add_flashcard_id(0)
    assert 0 in group.get_flashcard_ids()


def test_delete_flashcard_id(group):
    """Test delete_flashcard_id()."""
    assert group.delete_flashcard_id(0)
    group.add_flashcard_id(0)
    assert not group.delete_flashcard_id(0)
