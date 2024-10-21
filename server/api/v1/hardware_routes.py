from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.hardware_schemas import NewHardwareRequest, HardwareResponse, UpdateHardwareRequest

router = APIRouter(prefix='/hardware')


@router.get(
    path='',
    status_code=200,
    responses={
        200: {'description': 'Lista de productos'},
    },
    description='Retorna una lista con todos los productos con sus respectivos datos.'
)
async def get_all(limit: Annotated[int, Query(gt=0, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[HardwareResponse]:
    return []


@router.get(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto encontrado'},
        422: {'description': 'Id no es un entero valido'},
    },
    description='Retorna producto con sus respectivos datos via id. Puede fallar si la ID ingresada no coincide con ningún producto.'
)
async def get_by_id(id: Annotated[int, Path(gt=0, le=1000)]) -> HardwareResponse:
    return {'id': id}


@router.post(
    path='',
    status_code=201,
    responses={
        201: {'description': 'Producto creado'},
        422: {'description': 'Id no es un entero valido'},
    },
    description='Crea producto agregandole sus datos e id. Puede fallar si el Body Param esta incompleto.'
)
async def create(new_product: NewHardwareRequest) -> HardwareResponse:
    return new_product


@router.patch(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto actualizado'},
        422: {'description': 'Id no es un entero valido'},
    },
    description='Actualiza datos del producto via id. Puede fallar si la ID ingresada no coincide con ningún producto.'
)
async def update(id: Annotated[int, Path(gt=0, le=1000)], product: UpdateHardwareRequest) -> HardwareResponse:
    return product


@router.delete(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto eliminado'},
        422: {'description': 'Id no es un entero valido'},
    },
    description='Elimina producto via id. Puede fallar si la ID ingresada no coincide con ningún producto.'
)
async def delete(id: Annotated[int, Path(gt=0, le=1000)]) -> None:
    return None
