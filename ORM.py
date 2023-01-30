import psycopg2


class BaseManager:
    connection = None
    cursor = None

    def __init__(self, manager, chunk_size: int = 2000):
        self.manager = manager
        self.chunk_size = chunk_size

    @classmethod
    def setConnection(cls, settings):
        cls.connection = psycopg2.connect(**settings)

    @classmethod
    def getCursor(cls):
        cls.cursor = cls.connection.cursor()
        return cls.cursor

    @classmethod
    def executeQuery(cls, query):
        cls.cursor.execute(query)
        cls.connection.commit()
        return cls.cursor

    def select(self, params):
        return self.executeQuery(query=f'SELECT {", ".join(params)} FROM employees').fetchmany(size=self.chunk_size)

    def insert(self):
        print('insert')

    def update(self):
        print("update")

    def delete(self):
        print("delete")


class MetaModel(type):
    manager = BaseManager

    def _get_manager(cls):
        return cls.manager(manager=cls)

    @property
    def model(cls):
        return cls._get_manager()


class BaseModel(metaclass=MetaModel):
    tablename = ''

