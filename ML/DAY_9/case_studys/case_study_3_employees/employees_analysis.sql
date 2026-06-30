-- ============================================================================
-- CASE STUDY 3 — EMPLOYEE DATABASE ANALYSIS
-- ----------------------------------------------------------------------------
-- Business context:
--   HR wants to review salaries by department. We use an employees table (from
--   the Day 9 notes, Section 27).
--
-- What you will practise here:
--   * Filtering on a TEXT column (department = 'IT')
--   * Filtering on a NUMERIC column (salary > 50000)
--   * Sorting with ORDER BY salary DESC to rank earners
--   * Reading an HR insight out of a ranked result
--
-- How to run this file:
--   * SQLite CLI:  sqlite3 < employees_analysis.sql
--   * Python:      conn.executescript(open("employees_analysis.sql").read())
--   * Or paste the queries into any SQL tool.
-- ============================================================================


-- ============================================================================
-- SETUP — build the table to query
-- (CREATE / INSERT are previewed here only to set up data; taught fully later.)
-- ============================================================================
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    EmpID      INTEGER PRIMARY KEY,   -- unique label for each employee
    Name       TEXT,
    Department TEXT,
    Salary     INTEGER
);

INSERT INTO employees VALUES (1, 'Asha',  'IT',      50000);
INSERT INTO employees VALUES (2, 'Ravi',  'HR',      55000);
INSERT INTO employees VALUES (3, 'Imran', 'IT',      40000);
INSERT INTO employees VALUES (4, 'Divya', 'Finance', 90000);
INSERT INTO employees VALUES (5, 'Karan', 'IT',      60000);


-- ============================================================================
-- 1. FILTER — IT department, ranked by salary
-- ============================================================================
-- WHERE on a text column keeps only IT staff; ORDER BY salary DESC ranks them
-- highest-paid first.
SELECT Name, Salary
FROM employees
WHERE Department = 'IT'
ORDER BY Salary DESC;

-- Expected output:
--   Name  | Salary
--   ------+-------
--   Karan | 60000
--   Asha  | 50000
--   Imran | 40000
--
-- INSIGHT:
-- Among IT staff, Karan is the highest paid, Imran the lowest — useful for
-- pay-equity reviews.


-- ============================================================================
-- 2. FILTER — high earners across the company
-- ============================================================================
-- A numeric filter on salary, ranked highest first, across all departments.
SELECT Name, Department, Salary
FROM employees
WHERE Salary > 50000
ORDER BY Salary DESC;

-- Expected output:
--   Name  | Department | Salary
--   ------+------------+-------
--   Divya | Finance    | 90000
--   Karan | IT         | 60000
--   Ravi  | HR         | 55000
--
-- INSIGHT & RECOMMENDATION:
-- Three employees earn above 50,000, led by Divya in Finance. This filtered,
-- ranked view supports budget planning and identifies senior staff — the same
-- kind of finding from the Day 6/8 employee analyses, now produced directly
-- from the database with SQL.
