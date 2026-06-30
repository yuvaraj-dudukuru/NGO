-- ============================================================
-- Mini Project: NorthRetail -- RUNNER (pure SQLite, no Python)
-- Builds the schema, loads the data, and runs every report.
--
-- Run from inside this folder:
--     sqlite3 :memory: ".read run_all.sql"
-- ============================================================
.mode column
.headers on

.read schema.sql
.read data.sql

-- Echo each query before its result set so output is self-describing.
.echo on
.read queries.sql
.echo off
