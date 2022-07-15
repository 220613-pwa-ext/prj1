from dotenv import dotenv_values
from psycopg_pool import ConnectionPool

config = dotenv_values(".env")

pool = ConnectionPool(
    'postgresql://' +
    config.get('user') + ':'
    + config.get('password') + '@' +
    config.get('host') + ':' +
    config.get('port') + '/' +
    config.get('dbname')
)

