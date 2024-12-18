from server.schemas import RegisterUser, TokenResponse, LoginUser, UserResponse, NewUserRequest, UpdateUserRequest
from server.exceptions import BadRequest
from server.repositories import UsersRepository
from server.services import UsersService
from server.handlers import jwt_handler
from server.enums import RoleEnum


class AuthService:

    def __init__(self):
        self.user_service = UsersService()
        self.user_repository = UsersRepository()

    def register(self, new_user: RegisterUser) -> TokenResponse:
        new_user_dict = new_user.model_dump()
        new_user_dict.update(role=RoleEnum.COMMON)
        user = self.user_service.create(NewUserRequest(**new_user_dict))

        # El role del primer usuario seria el superadmin, de lo contrario es common
        if user.id == 1:
            user.role = RoleEnum.SUPER
            user_dict =user.model_dump()
            del user_dict['created']
            del user_dict['updated']
            del user_dict['id']
            updated_user = UpdateUserRequest(**user_dict)
            user = self.user_service.update(user_id=1, user=updated_user)

        return self.__get_token(user)

    def login(self, credentials: LoginUser) -> TokenResponse:
        user = self.user_repository.get_by_username(credentials.username)
        if user is None:
            raise BadRequest('Error en username/password')
        is_password_ok = self.user_repository.check_password(
            user['id'], credentials.password)
        if not is_password_ok:
            raise BadRequest('Error en username/password')
        response = TokenResponse.model_validate({'user': user})
        response.access_token = self.__get_user_token(
            response.user.id, response.user.role)
        return response

    def __get_token(self, user: UserResponse) -> TokenResponse:
        token = self.__get_user_token(user.id, user.role)
        return TokenResponse(
            access_token=token,
            user=user,
        )

    def __get_user_token(self, user_id, user_role) -> str:
        payload = {
            'user_id': str(user_id),
            'role': user_role,
        }
        return jwt_handler.encode(payload)
