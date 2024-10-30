from typing import List

from server.schemas import HardwareResponse, NewHardwareRequest, UpdateHardwareRequest
from server.exceptions import NotFound
from server.repositories import HardwareRepository


class HardwareService:

    def __init__(self) -> None:
        self.repository = HardwareRepository()

    def create(self, new_product: NewHardwareRequest) -> HardwareResponse:
        product_dict = self.repository.create(new_product.model_dump())
        return HardwareResponse(**product_dict)

    def get_all(self, limit: int, offset: int) -> List[HardwareResponse]:
        product_list = self.repository.get_all(limit, offset)
        return [HardwareResponse(**product) for product in product_list]

    def get_by_id(self, id: int) -> HardwareResponse:
        product = self.repository.get_by_id(id)
        if product is None:
            raise NotFound(f'Producto con Id N°{id} no se ha encontrado')
        return HardwareResponse(**product)

    def update(self, id: int, product: UpdateHardwareRequest) -> HardwareResponse:
        updated_product = self.repository.update(
            id, product.model_dump(exclude_none=True))
        if updated_product is None:
            raise NotFound(f'Producto con Id N°{id} no se ha encontrado')
        return HardwareResponse(**updated_product)

    def delete(self, id: int) -> None:
        if not self.repository.delete(id):
            raise NotFound(f'Producto con Id N°{id} no se ha encontrado')
