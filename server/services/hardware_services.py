from typing import List

from server.schemas.hardware_schemas import HardwareResponse, NewHardwareRequest, UpdateHardwareRequest
from server.exceptions.client_exceptions import NotFound


class HardwareService:
    last_id = 0
    fake_db: List[dict] = []

    def __init__(self) -> None:
        pass

    def create(self, new_product: NewHardwareRequest) -> HardwareResponse:
        product_dict = self.__fake_create(new_product.model_dump())
        return HardwareResponse(**product_dict)

    def get_all(self, limit: int, offset: int) -> List[HardwareResponse]:
        product_list = self.__fake_get_all(limit, offset)
        return [HardwareResponse(**product) for product in product_list]

    def get_by_id(self, id: int) -> HardwareResponse:
        product = self.__fake_get_by_id(id)
        if product is None:
            raise NotFound(f'Producto con Id N°{id} no se ha encontrado')
        return HardwareResponse(**product)

    def update(self, id: int, product: UpdateHardwareRequest) -> HardwareResponse:
        updated_product = self.__fake_update(id, product.model_dump(exclude_none=True))
        if updated_product is None:
            raise NotFound(f'Producto con Id N°{id} no se ha encontrado')
        return HardwareResponse(**updated_product)

    def delete(self, id: int) -> None:
        if not self.__fake_delete(id):
            raise NotFound(f'Producto con Id N°{id} no se ha encontrado')

    # FAKEMETHODS#

    def __fake_create(self, new_product: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        HardwareService.last_id += 1
        new_product.update(
            id=HardwareService.last_id,
            created_at=now,
            updated_at=now
        )
        HardwareService.fake_db.append(new_product)
        return new_product

    def __fake_get_all(self, limit: int, offset: int) -> List[dict]:
        db_size = len(HardwareService.fake_db)
        first_index = min(db_size, offset)
        last_index = max((db_size-first_index), limit)
        return HardwareService.fake_db[first_index:last_index]

    def __fake_get_by_id(self, id: int) -> dict | None:
        for product in HardwareService.fake_db:
            if product['id'] == id:
                return product

    def __fake_update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_product = self.__fake_get_by_id(id)
        if current_product is None:
            return
        current_product.update(**new_data, updated=now)
        return current_product

    def __fake_delete(self, id: int) -> bool:
        current_product = self.__fake_get_by_id(id)
        if current_product is None:
            return False
        HardwareService.fake_db.remove(current_product)
        return True
