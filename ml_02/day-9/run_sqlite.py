#!/usr/bin/env python3
"""Run `sample.sql` using sqlite3 and print results."""
from pathlib import Path
import sqlite3
import sys

root = Path(__file__).parent
sql_path = root / 'sample.sql'

if not sql_path.exists():
    print(f"SQL file not found: {sql_path}")
    sys.exit(1)

sql = sql_path.read_text()

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
try:
    cur.executescript(sql)
except Exception as e:
    print('Error executing SQL:', e)
    sys.exit(1)

cur.execute('SELECT id, name, age FROM sample_table')
rows = cur.fetchall()
print('Inserted rows:')
for r in rows:
    print(r)

conn.close()
