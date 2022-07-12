from dotenv import dotenv_values
from psycopg_pool import ConnectionPool

config = dotenv_values(".env")

pool = ConnectionPool(
    'postgresql://' +
    config['user'] + ':'
    + config['password'] + '@' +
    config['host'] + ':' +
    config['port'] + '/' +
    config['dbname']
)

