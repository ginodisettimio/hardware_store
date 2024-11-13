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

    def get_by_id(self, product_id: int) -> HardwareResponse:
        product = self.repository.get_by_id(product_id)
        if product is None:
            raise NotFound(f'Producto con id #{id} no se ha encontrado')
        return HardwareResponse(**product)

    def update(self, product_id: int, product: UpdateHardwareRequest) -> HardwareResponse:
        updated_product = self.repository.update(
            product_id, product.model_dump(exclude_none=True))
        if updated_product is None:
            raise NotFound(f'Producto con id #{product_id} no se ha encontrado')
        return HardwareResponse(**updated_product)

    def delete(self, product_id: int) -> None:
        if not self.repository.delete(product_id):
            raise NotFound(f'Producto con id #{product_id} no se ha encontrado')
