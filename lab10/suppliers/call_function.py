import psycopg2
from config import load_config

def get_parts(vendor_id):
    """Get parts provided by a vendor specified by vendor_id"""
    parts = []
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # Call PostgreSQL function
                cur.callproc('get_parts_by_vendor', (vendor_id,))
                # Fetch all results
                rows = cur.fetchall()
                for row in rows:
                    parts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print("❌ Error:", error)
    return parts

if __name__ == '__main__':
    vendor_id = 1
    parts = get_parts(vendor_id)
    print(f"✅ Parts for Vendor {vendor_id}:")
    for part in parts:
        print(f"  - ID: {part[0]}, Name: {part[1]}")
  