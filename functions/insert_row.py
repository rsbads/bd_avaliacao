import sqlite3

def insert_one_row(database_name: str, table_name: str, columns_name: str, values: tuple) -> None:
    database_name = f'{database_name}.db'
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    placeholders = ', '.join('?' * len(values))
    query = f"""
        INSERT INTO {table_name} ({columns_name})
        VALUES ({placeholders})
    """
    cursor.execute(query, values)
    conn.commit()
    conn.close()