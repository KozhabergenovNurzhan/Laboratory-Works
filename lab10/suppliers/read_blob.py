import psycopg2
from config import load_config

def read_blob(part_id, path_to_dir):
    """ Read BLOB and save it to a file """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, file_extension, drawing_data
                    FROM part_drawings
                    INNER JOIN parts ON parts.part_id = part_drawings.part_id
                    WHERE parts.part_id = %s
                """, (part_id,))
                blob = cur.fetchone()
                if blob:
                    file_path = f"{path_to_dir}{blob[0]}.{blob[1]}"
                    with open(file_path, 'wb') as output:
                        output.write(blob[2])
                    print(f"✅ File written to {file_path}")
                else:
                    print(f"⚠️ No drawing found for part_id={part_id}")
    except Exception as e:
        print("❌ Error reading blob:", e)

if __name__ == '__main__':
    read_blob(1, 'images/output/')
    read_blob(2, 'images/output/')
