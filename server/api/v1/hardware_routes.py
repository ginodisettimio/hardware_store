from fastapi import APIRouter

router = APIRouter(prefix='/hardware')


@router.get(
    path='',
    status_code=200,
    responses={
        200: {'description': 'Lista de productos'},
    },
    description='Retorna una lista con todos los productos con sus respectivos datos.'
)
async def get_all() -> list:
    return []


@router.get(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto encontrado'},
        422: {'description': 'Id tiene que ser un entero'},
    },
    description='Retorna producto con sus respectivos datos via id.'
)
async def get_by_id(id: int) -> dict:
    return {'id': id}


@router.post(
    path='',
    status_code=201,
    responses={
        201: {'description': 'Producto creado'}
    },
    description='Crea producto agregandole sus datos e id.'
)
async def create() -> dict:
    return {}


@router.patch(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto actualizado.'},
        422: {'description': 'Id tiene que ser un entero'},
    },
    description='Actualiza datos del producto via id.'
)
async def update(id: int) -> dict:
    return {'id': id}


@router.delete(
    path='/{id}',
    status_code=200,
    responses={
        200: {'description': 'Producto eliminado.'},
        422: {'description': 'Id tiene que ser un entero'},
    },
    description='Elimina producto via id.'
)
async def delete(id: int) -> None:
    return None
