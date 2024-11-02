from server.database.database_connection import DatabaseConnection
from server.database.models import BaseModel
from server.configs import app_settings

database_connection = DatabaseConnection(app_settings.DB_CONNECTION)


def create_tables():
    BaseModel.metadata.create_all(bind=database_connection.engine)
