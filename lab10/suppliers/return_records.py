import psycopg2
from config import load_config

def search_contacts(pattern):
  config = load_config()
  results = []
  try:
      with psycopg2.connect(**config) as conn:
          with conn.cursor() as cur:
              cur.callproc('search_contacts', (pattern,))
              rows = cur.fetchall()
              for row in rows:
                  results.append(row)
  except (Exception, psycopg2.DatabaseError) as error:
      print("Error:", error)
  return results


if __name__ == '__main__':
  pattern = input("Enter search pattern: ")
  results = search_contacts(pattern)
  for r in results:
      print(f"ID: {r[0]}, Name: {r[1]}, Surname: {r[2]}, Phone: {r[3]}")
