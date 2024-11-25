from typing import List

from server.schemas import HardwareResponse, NewHardwareRequest, UpdateHardwareRequest, BuyedHardwareResponse, DecodedJwt
from server.exceptions import NotFound
from server.repositories import HardwareRepository


class HardwareService:

    def __init__(self) -> None:
        self.repository = HardwareRepository()

    def create(self, new_product: NewHardwareRequest) -> HardwareResponse:
        new_product_dict = new_product.model_dump()
        product_dict = self.repository.create(new_product_dict)
        return HardwareResponse(**product_dict)

    def get_list(self, limit: int, offset: int) -> List[HardwareResponse]:
        product_list = self.repository.get_list(limit, offset)
        return [HardwareResponse(**product) for product in product_list]

    def get_buyed_products_list(self, limit: int, offset: int, token: DecodedJwt) -> List[BuyedHardwareResponse]:
        product_list = self.repository.get_buyed_products_list(
            limit, offset, token)
        return [BuyedHardwareResponse(**product) for product in product_list]

    def get_by_id(self, product_id: int) -> BuyedHardwareResponse:
        product = self.repository.get_by_id(product_id)
        if product is None:
            raise NotFound(f'Producto con id #{id} no se ha encontrado')
        return BuyedHardwareResponse(**product)

    def update(self, product_id: int, product: UpdateHardwareRequest) -> BuyedHardwareResponse:
        updated_product = self.repository.update(
            product_id, product.model_dump(exclude_none=True))
        if updated_product is None:
            raise NotFound(f'Producto con id #{
                           product_id} no se ha encontrado')
        return HardwareResponse(**updated_product)

    def delete(self, product_id: int) -> None:
        if not self.repository.delete(product_id):
            raise NotFound(f'Producto con id #{
                           product_id} no se ha encontrado')
