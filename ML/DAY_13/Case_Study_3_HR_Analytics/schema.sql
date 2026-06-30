-- ============================================================
-- Case Study 3: HR Analytics
-- File: schema.sql  -- table definition
-- ============================================================

-- Start clean so the script can be re-run safely.
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    EmpID            INTEGER PRIMARY KEY,
    Name             TEXT    NOT NULL,
    Department       TEXT    NOT NULL,   -- 'IT', 'HR', 'Finance'
    Salary           INTEGER NOT NULL,
    PerformanceScore INTEGER NOT NULL    -- 0..100
);
