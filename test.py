from main import *

settings = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'ormtest',
    'user': 'root',
    'password': 'root'
}

BaseModel.model.setConnection(settings=settings)
BaseModel.model.getCursor()
print(BaseModel.model.select({"id", "salary"}))

