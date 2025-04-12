import psycopg2
from config import load_config

def delete_by_user_or_phone(identifier):
  config = load_config()
  try:
      with psycopg2.connect(**config) as conn:
          with conn.cursor() as cur:
              cur.execute("CALL delete_by_user_or_phone(%s);", (identifier,))
              conn.commit()
              print(f"🗑️ Deleted user or phone matching '{identifier}'.")
  except Exception as e:
      print("❌ Error deleting entry:", e)
