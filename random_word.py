# the function:
#   - selects a random word with the "learn" status
#   - returns a dict() with "word", "meaning", "status"
#   - works only with db
#   - returns None if no words with "learn" status
#   - doesn't change the status of words
#   - doesn't interact with UI

import sqlite3
import config


def get_random_word():
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT word, details, status FROM Words WHERE status='learn' ORDER BY RANDOM() LIMIT 1"
        )
        row = cur.fetchone()
        if row is None:
            return None

        word_data = {"word": row[0], "meaning": row[1], "status": row[2]}
        return word_data
