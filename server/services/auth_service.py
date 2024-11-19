from server.schemas import RegisterUser, TokenResponse, LoginUser, UserResponse
from server.exceptions import BadRequest
from server.repositories import UsersRepository
from server.services import UsersService
from server.handlers.jwt_handler import jwt_handler


class AuthService:

    def __init__(self):
        self.user_service = UsersService()
        self.user_repository = UsersRepository()

    def register(self, new_user: RegisterUser) -> TokenResponse:
        user = self.user_service.create(new_user)
        return self.__get_token(user)
    
    def login(self, credentials: LoginUser) -> TokenResponse:
        user = self.user_repository.get_by_username(credentials.username)
        if user is None:
            raise BadRequest('Error en username/password')
        is_password_ok = self.user_repository.check_password(user['id'], credentials.password)
        if not is_password_ok:
            raise BadRequest('Error en username/password')
        response = TokenResponse.model_validate({'user': user})
        response.acces_token = self.__get_user_token(response.user.id, response.user.role)
        return response

    def __get_token(self, user: UserResponse) -> TokenResponse:
        token = self.__get_user_token(user.id, user.role)
        return TokenResponse(
            acces_token=token,
            user=user,
        )

    def __get_user_token(self, user_id, user_role) -> str:
        payload = {
            'user_id': str(user_id),
            'role': user_role,
        }
        return jwt_handler.encode(payload)
