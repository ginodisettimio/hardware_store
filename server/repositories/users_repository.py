from typing import List

from sqlalchemy.exc import IntegrityError

from server.database import database_connection
from server.database.models import UserModel
from server.exceptions import UniqFieldException


class UsersRepository:
    def __init__(self) -> None:
        self.database = database_connection.session

    def create(self, new_user_dict: dict) -> dict:
        new_user = UserModel(**new_user_dict)
        self.database.add(new_user)
        try:
            self.database.commit()
        except IntegrityError as ie:
            self.database.rollback()
            raise UniqFieldException(ie.args)
        self.database.refresh(new_user)
        return new_user.to_dict()

    def get_all(self, limit: int, offset: int) -> list[dict]:
        users = self.database.query(UserModel).order_by(
            'id').offset(offset).limit(limit)
        return [user.to_dict() for user in users]

    def get_by_id(self, user_id: int) -> dict | None:
        user = self.__get_one(user_id)
        if user is None:
            return
        return user.to_dict()
    
    def get_by_username(self, username: str) -> dict | None:
        user = self.database.query(UserModel).filter_by(username=username).first()
        if user is None:
            return
        return user.to_dict()

    def update(self, user_id: int, new_data: dict) -> dict | None:
        user = self.__get_one(user_id)
        if user is None:
            return
        for field in new_data.keys():
            setattr(user, field, new_data[field])
        self.database.commit()
        self.database.refresh(user)
        return user.to_dict()

    def delete(self, user_id: int) -> bool:
        user = self.__get_one(user_id)
        if user is None:
            return False
        self.database.delete(user)
        self.database.commit()
        return True
    
    def check_password(self, user_id: int, plain_password: str) -> bool:
        user = self.__get_one(user_id)
        if user is None: 
            return False
        return user.check_password(plain_password)

    def __get_one(self, user_id: int) -> UserModel | None:
        return self.database.query(UserModel).filter_by(id=user_id).first()
    