import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_connection():
  return mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
  )

def close_connection(connection, cursor):
  if cursor:
    cursor.close()
  if connection:
    connection.close()

def get_table(table, filters=None, order=None, limit=None):
  connection = None
  cursor = None
  try:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = f"SELECT * FROM {table}"
    params = []
    if filters:
      query += " WHERE "
      conditions = []
      for key, value in filters.items():
        conditions.append(f"{key} = %s")
        params.append(value)
      query += " AND ".join(conditions)

    if order:
      query += f" ORDER BY {order}"

    if limit:
      query += " LIMIT %s"
      params.append(limit)

    cursor.execute(query, params)    
    print(cursor.statement)

    rows = cursor.fetchall()
    return rows
  except Exception as e:
    print(f"Error: {e}")
    return []
  finally:
    close_connection(connection, cursor)

def get_stock_prices(filters=None, order=None, limit=100):
  return get_table('stock', filters, order, limit)

if __name__ == "__main__":
  stock_prices = get_stock_prices(filters={'symbol': "btcusd"}, order="date ASC", limit=10)
  print(stock_prices)