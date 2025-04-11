import psycopg2
from config import load_config

def add_part(part_name, vendor_name):
    """ Call stored procedure to insert part and vendor """
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_part(%s, %s);', (part_name, vendor_name))
            conn.commit()
            print(f"✅ Inserted part '{part_name}' and vendor '{vendor_name}'")
    except (Exception, psycopg2.DatabaseError) as error:
        print("❌ Error:", error)

if __name__ == '__main__':
    add_part('OLED', 'LG')
