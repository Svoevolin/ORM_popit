import psycopg2

from ormType import ORMType
from ormConstraint import ORMConstraint

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

    @classmethod
    def column(cls, concreteVarType, concreteConstraint = None):
        return f" {concreteVarType}" + f" {concreteConstraint}" if concreteConstraint is not None else ""

    def createTable(self, column):
        fields = list(column.keys())
        modificators = list(column.values())
        print(fields)
        print(modificators)
        attr = []
        for i in range(len(fields)):
            attr.append(f'{fields[i]} {modificators[i]}')
        self.executeQuery(f'CREATE TABLE {self.manager.tablename} ({", ".join(attr)})')

    def select(self, field=None):
        if field is not None:
            query = f'SELECT {", ".join(field)} FROM {self.manager.tablename}'
        else:
            query = f'SELECT * FROM {self.manager.tablename}'

        return self.executeQuery(query).fetchmany(size=self.chunk_size)

    def insert(self, data):

        fields = data.keys()
        values = data.values()

        self.executeQuery(query=f"INSERT INTO {', '.join(fields)} VALUES {', '.join(values)}")


    def update(self, newData):

        fields = newData.keys()
        values = newData.values()

        query = f'UPDATE {self.manager.tablename} SET'
        attr = []
        for i in range(len(fields)):
            attr.append(f"{fields[i]}={values[i]}")
        self.executeQuery(query + ", ".join(attr))


    def delete(self):
        self.executeQuery(f'DELETE FROM {self.manager.tablename}')

    def drop(self):
        self.executeQuery(f'DROP TABLE IF EXISTS {self.manager.tablename}')



class MetaModel(type):
    manager = BaseManager

    def _get_manager(cls):
        return cls.manager(manager=cls)

    @property
    def model(cls):
        return cls._get_manager()


class BaseModel(metaclass=MetaModel):
    tablename = ''

# ------------------------------------------------------
class C(BaseModel):
    tablename = "testCode"
    id = BaseManager.column(ORMType.SERIAL(), ORMConstraint.PRIMARYKEY())
    name = BaseManager.column(ORMType.VARCHAR(50), ORMConstraint.NOTNULL())





