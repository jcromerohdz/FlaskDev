import uuid
import datetime
from flask import session
from src.common.database import Database


class User(object):
    def __init__(self, email, pasword, _id=None):
        self.email = get_by_email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, self):
        data = Database.find_one("users": {"email": self.email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, self):
        data = Database.find_one("users": {"_id": self._id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user =  User.get_by_email(email)
        if user is not None:
            #We can check the password
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user =  cls.get_by_email(email)
        if user is not None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout(user_email):
        session['email'] = None

    def get_blogs(self):
        pass

    def json(self):
        return{
            "email": self.email,
            "_id": self._id
        }

    def save_to_mongo(self):
        pass
