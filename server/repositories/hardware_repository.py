from typing import List


class HardwareRepository:
    last_id = 0
    fake_db: List[dict] = []

    def create(self, new_product: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        self.last_id += 1
        new_product.update(
            id=self.last_id,
            created_at=now,
            updated_at=now
        )
        self.fake_db.append(new_product)
        return new_product

    def get_all(self, limit: int, offset: int) -> List[dict]:
        db_size = len(self.fake_db)
        first_index = min(db_size, offset)
        last_index = max((db_size-first_index), limit)
        return self.fake_db[first_index:last_index]

    def get_by_id(self, id: int) -> dict | None:
        for product in self.fake_db:
            if product['id'] == id:
                return product

    def update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_product = self.get_by_id(id)
        if current_product is None:
            return
        current_product.update(**new_data, updated=now)
        return current_product

    def delete(self, id: int) -> bool:
        current_product = self.get_by_id(id)
        if current_product is None:
            return False
        self.fake_db.remove(current_product)
        return True
