from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


class DatabaseConnection:
    def __init__(self, str_connection: str) -> None:
        self.str_connection: str = str_connection
        self.__engine: Engine = None
        self.__session: Session = None

    @property
    def session(self):
        if self.__session is None:
            Session = sessionmaker(bind=self.engine)
            self.__session = Session()
        return self.__session

    @property
    def engine(self):
        if self.__engine is None:
            self.__engine = create_engine(self.str_connection)
        return self.__engine

    def connect(self) -> bool:
        try:
            self.session.connection()
            return True
        except Exception:
            print('\033[91m', 'Database connection failed', '\033[0m')
            return False

    def disconnect(self) -> None:
        if self.session:
            self.session.close()
