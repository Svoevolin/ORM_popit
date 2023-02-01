import psycopg2

DB_SETTINGS = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'ormtest',
    'user': 'root',
    'password': 'root'
}

# connection = psycopg2.connect(**DB_SETTINGS)
# cursor = connection.cursor()
#
# cursor.execute('SELECT * FROM employees')
# print(cursor.fetchmany(size=2000))




# # Create employees table
# query = """
#     CREATE TABLE employees (
#         id SERIAL PRIMARY KEY,
#         first_name varchar(255),
#         last_name varchar(255),
#         salary numeric(10, 2),
#         grade varchar(10)
#     )
# """
# cursor.execute(query)
#
# # # Insert some data
# query = """
#     INSERT INTO employees (first_name, last_name, salary, grade)
#         VALUES
#             ('l', '1', 13000, 'L2'),
#             ('b', '2', 16000, 'L3');
# """
# cursor.execute(query)
#
# connection.commit()