import sqlite3
from datetime import datetime
import sys
import time
import random
import tkinter as tk
import yaml
import logging
import config

# temporary config log
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


def load_words_from_yaml():
    # 1. Read YAML
    with open(config.YAML_FILE, "r") as file_yaml:  # created or overwriten
        try:
            data = yaml.safe_load(file_yaml)  # to parse yaml
        except FileNotFoundError:  # catch a specific exception
            logger.error("YAML file '%s' not found", config.YAML_FILE)
        except yaml.YAMLError as e:  # catch a specific exception
            logger.error("Syntax error in YAML file: %s", e)
            return

        if data is None:
            logger.warning("add_words.yaml is empty — no new words to import")
            return

        if not isinstance(data, list):
            logger.error(
                "Invalid data format in '%s': expected a list of items but got %s",
                config.YAML_FILE,
                type(data).__name__,
            )
            return

    # 2. Work with database
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()

        # statistics
        added = 0
        skipped = 0
        errors = 0

        for ls in data:
            word_info = ls.get("word") if isinstance(ls, dict) and "word" in ls else ls
            # Validate each item structure. continue -so that the cycle is not interrupted
            if not isinstance(ls, dict):
                logger.warning(
                    "Invalid data format for word '%s': expected a dictionary",
                    word_info,
                )
                errors += 1
                continue
            if "word" not in ls:
                logger.warning("Missing 'word' key in item: '%s'", word_info)
                errors += 1
                continue
            if "meaning" not in ls:
                logger.warning("Missing 'meaning' key for word '%s'", word_info)
                errors += 1
                continue
            if not isinstance(ls["word"], str):
                logger.warning("Wrong type for 'word' in item: '%s'", word_info)
                errors += 1
                continue
            if not isinstance(ls["meaning"], str):
                logger.warning("Wrong type for 'meaning' in item: '%s'", word_info)
                errors += 1
                continue

            word = ls["word"]
            details = ls["meaning"]

            # Check duplicates
            cur.execute("SELECT word FROM Words WHERE word=?", (word,))
            result = cur.fetchone()
            if result:
                logger.info("Word '%s' already in database", word_info)
                skipped += 1
                continue

            # Insert new record
            cur.execute(
                "INSERT OR IGNORE INTO Words (word,details,status,created_at) VALUES (?,?, 'learn',?)",
                (word, details, datetime.now()),
            )
            added += 1
        conn.commit()
    logger.info("Added: '%s' | Skipped: '%s' | Errors: '%s'", added, skipped, errors)
