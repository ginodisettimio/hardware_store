from typing import List

# from server.external_api import hardware_api_client
from server.database import database_connection
from server.database.models.hardware_model import HardwareModel


class HardwareRepository:
    def __init__(self) -> None:
        self.database = database_connection.session

    def create(self, new_product: dict) -> dict:
        # from datetime import datetime
        # now = datetime.now()
        # self.last_id += 1
        # new_product.update(
        #     id=self.last_id,
        #     created_at=now,
        #     updated_at=now
        # )
        # self.fake_db.append(new_product)
        # return new_product
        new_product = HardwareModel(**new_product)
        self.database.add(new_product)
        self.database.commit()
        self.database.refresh(new_product)
        return self.__to_dict(new_product)

    def get_all(self, limit: int, offset: int) -> List[dict]:
        # db_size = len(self.fake_db)
        # first_index = min(db_size, offset)
        # last_index = max((db_size - first_index), limit)
        # return self.fake_db[first_index:last_index]
        # #return hardware_api_client.get_all(limit, offset)}
        products = self.database.query(HardwareModel).order_by(
            'id').offset(offset).limit(limit)
        return [self.__to_dict(product) for product in products]

    def get_by_id(self, id: int) -> dict | None:
        # for product in self.fake_db:
        #     if product['id'] == id:
        #         return product
        product = self.__get_one(id)
        if product is None:
            return
        return self.__to_dict(product)

    def update(self, id: int, new_data: dict) -> dict | None:
        # from datetime import datetime
        # now = datetime.now()
        # current_product = self.get_by_id(id)
        # if current_product is None:
        #     return
        # current_product.update(**new_data, updated=now)
        # return current_product
        product = self.__get_one(id)
        if product is None:
            return
        for field in new_data.keys():
            setattr(product, field, new_data[field])
        self.database.commit()
        self.database.refresh(product)
        return self.__to_dict(product)

    def delete(self, id: int) -> bool:
        # current_product = self.get_by_id(id)
        # if current_product is None:
        #     return False
        # self.fake_db.remove(current_product)
        # return True
        product = self.__get_one(id)
        if product is None:
            return False
        self.database.delete(product)
        self.database.commit()
        return True

    def __get_one(self, id: int) -> dict:
        return self.database.query(HardwareModel).filter_by(id=id).first()

    def __to_dict(self, product: HardwareModel) -> dict:
        return {
            column.name: getattr(product, column.name)
            for column in HardwareModel.__table__.columns
        }
