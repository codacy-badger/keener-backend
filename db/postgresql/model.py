"""Represent the models used in our PostgreSQL tables."""
from server.server import db

user_group_table = Table("user_group",
                         db.Column("user_id",
                                   db.Integer,
                                   db.ForeignKey("user_table.id"),
                                   primary_key=True),
                         db.Column("group_id",
                                   db.Integer,
                                   db.ForeignKey("group_table.id"),
                                   primary_key=True))


class UserModel(db.Model):
    """Model for the user table."""

    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    given_name = db.Column(db.String())
    picture_url = db.Column(db.String())
    flashcards = db.relationship("FlashcardModel", backref="user",
                                 lazy=True)
    groups = db.relationship("GroupModel",
                             secondary=user_group_table,
                             back_populates="users")


class GroupModel(db.Model):
    """Model for the group table."""

    __tablename__ = "group_table"

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(String(), nullable=False)
    users = db.relationship("UserModel",
                            secondary=user_group_table,
                            back_populates="groups")


class FlashcardModel(db.Model):
    """Model for the flashcard table."""

    __tablename__ = "flashcard_table"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String())
    group_id = db.Column(db.Integer, db.ForeignKey("group_table.id"),
                         nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("user_table.id"),
                           nullable=False)
