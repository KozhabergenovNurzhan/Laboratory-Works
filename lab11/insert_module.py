import psycopg2
from config import load_config

def insert_many_users(names, phones):
  config = load_config()
  invalid = []
  try:
      with psycopg2.connect(**config) as conn:
          with conn.cursor() as cur:
              cur.callproc('insert_many_users', (names, phones))
              invalid = cur.fetchone()[0] 
              print("✅ Inserted successfully. Invalid entries:", invalid)
  except Exception as e:
      print("❌ Error during bulk insert:", e)
  return invalid
