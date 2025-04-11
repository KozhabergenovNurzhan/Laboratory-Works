import psycopg2
from config import load_config

def get_or_create_user(username):
    """Return user_id, create user if not exists."""
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
                return cur.fetchone()[0]

def save_score(user_id, score, level):
    """Insert current score and level into the database."""
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_scores (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))

def get_last_score(user_id):
    """Return the latest saved score and level for a user, if exists."""
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level
                FROM user_scores
                WHERE user_id = %s
                ORDER BY saved_at DESC
                LIMIT 1
            """, (user_id,))
            return cur.fetchone()  # returns (score, level) or None

def get_top_scores(limit=5):
    """Return top scores across all users (by score then level)."""
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT u.username, s.score, s.level, s.saved_at
                FROM user_scores s
                JOIN users u ON s.user_id = u.user_id
                ORDER BY s.score DESC, s.level DESC, s.saved_at DESC
                LIMIT %s
            """, (limit,))
            return cur.fetchall()

