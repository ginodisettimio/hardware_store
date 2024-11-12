from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas import NewUserRequest, UserResponse, UpdateUserRequest
from server.controllers import UsersController
from server.exceptions import UnproccesableEntity, NotFound, InternalServerError

router = APIRouter(prefix='/users')

router.responses = {
    500: InternalServerError.as_dict(),
    404: NotFound.as_dict(),
    422: UnproccesableEntity.as_dict(),
}
controller = UsersController()


@router.post(
    path='',
    status_code=201,
    responses={
        201: {'description': 'Usuario creado'},
    },
    description='Crea usuario agregandole sus datos e id. Puede fallar si el Body Param esta incompleto.'
)
async def create(new_user: NewUserRequest) -> UserResponse:
    return controller.create(new_user)


@router.get(
    path='',
    status_code=200,
    responses={
        200: {'description': 'Lista de usuarios'},
    },
    description='Retorna una lista con todos los usuarios con sus respectivos datos.'
)
async def get_all(limit: Annotated[int, Query(gt=0, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[UserResponse]:
    return controller.get_all(limit, offset)


@router.get(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Usuario encontrado'},
    },
    description='Retorna usuario con sus respectivos datos via id. Puede fallar si la ID ingresada no coincide con ningún usuario.'
)
async def get_by_id(id: Annotated[int, Path(gt=0)]) -> UserResponse:
    return controller.get_by_id(id)


@router.patch(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Usuario actualizado'},
    },
    description='Actualiza datos del usuario via id. Puede fallar si la ID ingresada no coincide con ningún usuario.'
)
async def update(id: Annotated[int, Path(gt=0, le=1000)], user: UpdateUserRequest) -> UserResponse:
    return controller.update(id, user)


@router.delete(
    path='/{id}',
    status_code=204,
    responses={
        204: {'description': 'Usuario eliminado'},
    },
    description='Elimina usuario via id. Puede fallar si la ID ingresada no coincide con ningún usuario.'
)
async def delete(id: Annotated[int, Path(gt=0, le=1000)]) -> None:
    return controller.delete(id)
