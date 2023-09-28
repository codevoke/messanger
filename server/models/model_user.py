"""users database model"""
from __future__ import annotations
from passlib.hash import pbkdf2_sha256

from .db import db


class UserModel(db.Model):
    """model of Users with main information about them"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    username = db.Column(db.String)
    age = db.Column(db.Integer)

    def json(self):
        """return public user data"""
        return {
            "id": self.id,
            "username": self.username,
            "age": self.age
        }

    @classmethod
    def get(cls, _id: int) -> UserModel | None:
        """return user object by id or abort 404"""
        return cls.query.filter(
            cls.id == _id
        ).first_or_404(description="user not found")

    @classmethod
    def auth(cls, login: str, password: str) -> UserModel | None:
        """
        return user object or raise NotFound error
        
        :login:     login of user to retrieve
        :password:  password of user to retrieve
        """

        return cls.query.filter(
            cls.login == login,
            cls.password == pbkdf2_sha256.hash(password)
        ).one_or_none()
    
    def put(self, password: str|None =None, username: str|None =None, age: int|None =None) -> None:
        """
        modify user data fields

        :password:  new password
        :username:  new username
        :age:       new age
        """
        self.password = password or self.password
        self.username = username or self.username
        self.age = age or self.age
