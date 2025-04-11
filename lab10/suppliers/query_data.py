import psycopg2
from config import load_config

# --------- FETCHONE() ----------
def get_vendors_one_by_one():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                print("🔹 Vendors (one by one):")
                row = cur.fetchone()
                while row:
                    print(row)
                    row = cur.fetchone()
    except Exception as e:
        print("Error:", e)


# --------- FETCHALL() ----------
def get_all_vendors():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                rows = cur.fetchall()
                print("🔹 All Vendors:")
                for row in rows:
                    print(row)
    except Exception as e:
        print("Error:", e)


# --------- FETCHMANY() ----------
def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_parts_and_vendors():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, vendor_name
                    FROM parts
                    INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
                    INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
                    ORDER BY part_name
                """)
                print("🔹 Parts and their vendors (5 at a time):")
                for row in iter_row(cur, size=5):
                    print(row)
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    get_vendors_one_by_one()
    print("\n" + "-"*50 + "\n")
    get_all_vendors()
    print("\n" + "-"*50 + "\n")
    get_parts_and_vendors()
