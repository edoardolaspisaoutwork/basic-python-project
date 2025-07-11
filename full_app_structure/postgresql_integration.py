import os
import psycopg_pool

def init_connection_pool():
    # db_params = {
    #     "host": os.getenv("DB_HOST"),
    #     "port": os.getenv("DB_PORT"),
    #     "dbname": os.getenv("DB_NAME"),
    #     "user": os.getenv("DB_USER"),
    #     "password": os.getenv("DB_PASSWORD"),
    # }
    db_params = {
        "host": "localhost",
        "port": "5432",
        "dbname": "postgres",
        "user": "root",
        "password": "root",
    }
    # Create a connection string
    conninfo = " ".join(f"{k}={v}" for k, v in db_params.items())
    print("Connecting to postgreSQL with params: " + conninfo)
    # Initialize the connection pool
    return psycopg_pool.ConnectionPool(conninfo, min_size=1, max_size=10, timeout=10)

