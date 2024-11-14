from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from server.schemas import LoginUser, RegisterUser, TokenResponse
from server.exceptions import InternalServerError, BadRequest
from server.controllers import AuthController

router = APIRouter(prefix='/auth')

router.responses = {
    500: InternalServerError.as_dict(),
}
controller = AuthController()


@router.post(
    path='/register',
    status_code=201,
    responses={
        201: {'description': 'Usuario registrado'},
        400: {'description': BadRequest.description}
    },
    description='Registra usuario.'
)
async def register_user(new_user: RegisterUser) -> TokenResponse:
    return controller.register(new_user)


@router.post(
    path='/login',
    status_code=200,
    responses={
        200: {'description': 'Usuario logueado'},
        400: {'description': BadRequest.description}
    },
    description='Loguea usuario.'
)
async def login_user(credentials: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    return controller.login(credentials)
