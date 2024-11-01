from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas import NewHardwareRequest, HardwareResponse, UpdateHardwareRequest
from server.controllers import HardwareController
from server.exceptions import UnproccesableEntity, NotFound, InternalServerError

router = APIRouter(prefix='/hardware')

router.responses = {
    500: InternalServerError.as_dict(),
    404: NotFound.as_dict(),
    422: UnproccesableEntity.as_dict(),
}
controller = HardwareController()


@router.post(
    path='',
    status_code=201,
    responses={
        201: {'description': 'Producto creado'},
    },
    description='Crea producto agregandole sus datos e id. Puede fallar si el Body Param esta incompleto.'
)
async def create(new_product: NewHardwareRequest) -> HardwareResponse:
    return controller.create(new_product)


@router.get(
    path='',
    status_code=200,
    responses={
        200: {'description': 'Lista de productos'},
    },
    description='Retorna una lista con todos los productos con sus respectivos datos.'
)
async def get_all(limit: Annotated[int, Query(gt=0, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[HardwareResponse]:
    return controller.get_all(limit, offset)


@router.get(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto encontrado'},
    },
    description='Retorna producto con sus respectivos datos via id. Puede fallar si la ID ingresada no coincide con ningún producto.'
)
async def get_by_id(id: Annotated[int, Path(gt=0)]) -> HardwareResponse:
    return controller.get_by_id(id)


@router.patch(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto actualizado'},
    },
    description='Actualiza datos del producto via id. Puede fallar si la ID ingresada no coincide con ningún producto.'
)
async def update(id: Annotated[int, Path(gt=0, le=1000)], product: UpdateHardwareRequest) -> HardwareResponse:
    return controller.update(id, product)


@router.delete(
    path='/{id}',
    status_code=204,
    responses={
        204: {'description': 'Producto eliminado'},
    },
    description='Elimina producto via id. Puede fallar si la ID ingresada no coincide con ningún producto.'
)
async def delete(id: Annotated[int, Path(gt=0, le=1000)]) -> None:
    return controller.delete(id)
