from typing import List

# from server.external_api import hardware_api_client
from server.database import database_connection
from server.database.models import HardwareModel
from server.schemas import DecodedJwt
from server.enums import ADMIN_ROLES


class HardwareRepository:
    def __init__(self) -> None:
        self.database = database_connection.session

    def create(self, new_product_dict: dict) -> dict:
        # from datetime import datetime
        # now = datetime.now()
        # self.last_id += 1
        # new_product.update(
        #     product_id=self.last_id,
        #     created_at=now,
        #     updated_at=now
        # )
        # self.fake_db.append(new_product)
        # return new_product
        new_product = HardwareModel(**new_product_dict)
        self.database.add(new_product)
        self.database.commit()
        self.database.refresh(new_product)
        return new_product.to_dict()

    def get_list(self, limit: int, offset: int) -> List[dict]:
        # db_size = len(self.fake_db)
        # first_index = min(db_size, offset)
        # last_index = max((db_size - first_index), limit)
        # return self.fake_db[first_index:last_index]
        # #return hardware_api_client.get_all(limit, offset)}
        products = self.database.query(HardwareModel).order_by(
            'id').offset(offset).limit(limit).all()
        return [product.to_dict() for product in products]

    def get_buyed_products_list(self, limit: int, offset: int, token: DecodedJwt) -> List[dict]:
        # db_size = len(self.fake_db)
        # first_index = min(db_size, offset)
        # last_index = max((db_size - first_index), limit)
        # return self.fake_db[first_index:last_index]
        # #return hardware_api_client.get_all(limit, offset)}
        if token.role in ADMIN_ROLES:
            products = self.database.query(HardwareModel).order_by(
                'id').offset(offset).limit(limit).all()
        else:
            products = self.database.query(HardwareModel).order_by(
                'id').filter_by(user_id=token.user_id).offset(offset).limit(limit).all()
        return [product.to_dict() for product in products]

    def get_by_id(self, product_id: int) -> dict | None:
        # for product in self.fake_db:
        #     if product['product_id'] == product_id:
        #         return product
        product = self.__get_one(product_id)
        if product is None:
            return
        return product.to_dict()

    def update(self, product_id: int, new_data: dict) -> dict | None:
        # from datetime import datetime
        # now = datetime.now()
        # current_product = self.get_by_id(product_id)
        # if current_product is None:
        #     return
        # current_product.update(**new_data, updated=now)
        # return current_product
        product = self.__get_one(product_id)
        if product is None:
            return
        for field in new_data.keys():
            setattr(product, field, new_data[field])
        self.database.commit()
        self.database.refresh(product)
        return product.to_dict()

    def delete(self, product_id: int) -> bool:
        # current_product = self.get_by_id(product_id)
        # if current_product is None:
        #     return False
        # self.fake_db.remove(current_product)
        # return True
        product = self.__get_one(product_id)
        if product is None:
            return False
        self.database.delete(product)
        self.database.commit()
        return True

    def __get_one(self, product_id: int) -> HardwareModel | None:
        return self.database.query(HardwareModel).filter_by(id=product_id).first()
