-- ============================================================
-- Case Study 1: Retail Sales Analysis -- RUNNER
-- Builds the schema, loads the data, and runs every query.
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
