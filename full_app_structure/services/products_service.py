from full_app_structure.postgresql_integration import init_connection_pool

connection_pool = init_connection_pool()

def fetch_all_products():
    with connection_pool.connection() as conn:
        return conn.execute("SELECT * FROM products").fetchall()