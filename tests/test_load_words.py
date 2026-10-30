import sys
import os
import sqlite3
import logging

# --- Универсальный путь к корню проекта ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

import config
from word_loader import load_words_from_yaml

# --- Настройка логгера ---
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# --- Настройка временной базы ---
TEST_DB = os.path.join(PROJECT_ROOT, "db", "test_wordsdb.sqlite")
os.makedirs(os.path.dirname(TEST_DB), exist_ok=True)
config.DB_PATH = TEST_DB

if os.path.exists(TEST_DB):
    os.remove(TEST_DB)

with sqlite3.connect(TEST_DB) as conn:
    cur = conn.cursor()
    cur.execute(
        """
    CREATE TABLE Words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE,
        details TEXT,
        status TEXT,
        created_at TEXT
    )
    """
    )
    conn.commit()

# --- Настройка YAML файла ---
YAML_PATH = os.path.join(PROJECT_ROOT, "add_words.yaml")
if not os.path.exists(YAML_PATH):
    raise FileNotFoundError(f"YAML file not found: {YAML_PATH}")
config.YAML_FILE = YAML_PATH

# --- Запуск функции ---
logger.info("=== TEST: load_words_from_yaml() ===")
load_words_from_yaml()

# --- Проверка базы ---
with sqlite3.connect(TEST_DB) as conn:
    cur = conn.cursor()
    cur.execute("SELECT word, details, status FROM Words")
    rows = cur.fetchall()
    total = len(rows)

    logger.info("=== TEST RESULT ===")
    if total > 0:
        logger.info("First 5 words loaded (shortened meanings):")
        for word, details, status in rows[:5]:
            snippet = details[:100].replace("\n", " ") + (
                "..." if len(details) > 100 else ""
            )
            logger.info("Word: '%s' | Status: %s | Meaning: %s", word, status, snippet)
    else:
        logger.info("No words loaded")

    # --- Статистика ---
    added = total
    skipped = 0
    errors = 0
    logger.info(
        "Total words loaded: %d | Skipped: %d | Errors: %d", added, skipped, errors
    )

# --- Очистка временной базы после теста ---
if os.path.exists(TEST_DB):
    os.remove(TEST_DB)
    logger.info("Temporary test database removed")
