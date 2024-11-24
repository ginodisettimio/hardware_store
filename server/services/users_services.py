from typing import List

from server.schemas import UserResponse, NewUserRequest, UpdateUserRequest
from server.exceptions import NotFound
from server.repositories import UsersRepository


class UsersService:

    def __init__(self) -> None:
        self.repository = UsersRepository()

    def create(self, new_user: NewUserRequest) -> UserResponse:
        user_dict = self.repository.create(new_user.model_dump())
        return UserResponse(**user_dict)

    def get_all(self, limit: int, offset: int) -> List[UserResponse]:
        user_list = self.repository.get_all(limit, offset)
        return [UserResponse(**user) for user in user_list]

    def get_by_id(self, user_id: int) -> UserResponse:
        user = self.repository.get_by_id(user_id)
        if user is None:
            raise NotFound(f'Usuario con id #{user_id} no se ha encontrado')
        return UserResponse(**user)

    def update(self, user_id: int, user: UpdateUserRequest) -> UserResponse:
        updated_user = self.repository.update(
            user_id, user.model_dump(exclude_none=True))
        if updated_user is None:
            raise NotFound(f'Usuario con id #{user_id} no se ha encontrado')
        return UserResponse(**updated_user)

    def delete(self, user_id: int) -> None:
        if not self.repository.delete(user_id):
            raise NotFound(f'Usuario con id #{user_id} no se ha encontrado')
