import mysql.connector
from mysql.connector import pooling

# Configura la conexión a MariaDB
db_config = {
    'host': 'localhost',  # Use 'localhost' if running MariaDB locally
    'user': 'root',
    'password': 'root',
    'database': 'geecoin',
    'port': 8888,  # Specify the port
    'collation': 'utf8mb4_general_ci'
}

# Pool de conexiones
db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_db_connection():
    return db_pool.get_connection()