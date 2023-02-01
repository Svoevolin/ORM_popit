from ORM import *

settings = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'ormtest',
    'user': 'root',
    'password': 'root'
}
class C(BaseModel):
    tablename = "testCode"
    id = BaseManager.column(ORMType.SERIAL(), ORMConstraint.PRIMARYKEY())
    name = BaseManager.column(ORMType.VARCHAR(50), ORMConstraint.NOTNULL())

c = C()
BaseModel.model.setConnection(settings=settings)
BaseModel.model.getCursor()
print(C.model.createTable({
    "id": c.id,
    "name": c.name
}))

