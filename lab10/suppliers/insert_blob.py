import psycopg2
from config import load_config

def write_blob(part_id, path_to_file, file_extension):
    """ Insert a BLOB (binary data) into the part_drawings table """
    # Load DB config
    params = load_config()

    # Read the file as binary
    with open(path_to_file, 'rb') as file:
        data = file.read()

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO part_drawings(part_id, file_extension, drawing_data)
                    VALUES (%s, %s, %s)
                """, (part_id, file_extension, psycopg2.Binary(data)))
            conn.commit()
            print(f"✅ Drawing for part {part_id} inserted.")
    except Exception as e:
        print("❌ Error inserting blob:", e)

if __name__ == '__main__':
    write_blob(1, 'images/input/simtray.png', 'png')
    write_blob(2, 'images/input/speaker.png', 'png')
