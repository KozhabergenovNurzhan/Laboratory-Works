import psycopg2
from config import load_config

def upsert_user(name, phone):
  config = load_config()
  try:
      with psycopg2.connect(**config) as conn:
          with conn.cursor() as cur:
              cur.execute("CALL upsert_user(%s, %s);", (name, phone))
              conn.commit()
              print(f"✅ User '{name}' inserted/updated successfully.")
  except Exception as error:
      print("❌ Error:", error)

if __name__ == '__main__':
  name = input("Enter user name: ")
  phone = input("Enter phone number: ")
  upsert_user(name, phone)
