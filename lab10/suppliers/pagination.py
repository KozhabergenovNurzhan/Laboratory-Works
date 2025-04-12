import psycopg2
from config import load_config

def get_paginated_contacts(limit, offset):
  config = load_config()
  try:
      with psycopg2.connect(**config) as conn:
          with conn.cursor() as cur:
              cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
              rows = cur.fetchall()
              print("\n📄 Paginated Contacts:")
              for row in rows:
                  print(row)
  except Exception as e:
      print("❌ Error fetching paginated contacts:", e)
