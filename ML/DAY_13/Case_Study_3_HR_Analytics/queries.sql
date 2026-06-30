-- ============================================================
-- Case Study 3: HR Analytics
-- File: queries.sql  -- the analytical queries
-- ============================================================

-- ------------------------------------------------------------
-- 24.1 Department Summary
-- Headcount, total/average salary and average performance per dept.
-- AVG(PerformanceScore) is ROUND-ed to 2 dp for clean display.
-- ------------------------------------------------------------
SELECT Department,
       COUNT(*)                        AS Headcount,
       SUM(Salary)                     AS TotalSalary,
       AVG(Salary)                     AS AvgSalary,
       ROUND(AVG(PerformanceScore), 2) AS AvgPerformance
FROM Employees
GROUP BY Department
ORDER BY AvgSalary DESC;

-- ------------------------------------------------------------
-- 24.2 High-Performing Departments
-- HAVING keeps only departments whose average score exceeds 75.
-- ------------------------------------------------------------
SELECT Department,
       ROUND(AVG(PerformanceScore), 2) AS AvgPerformance
FROM Employees
GROUP BY Department
HAVING AVG(PerformanceScore) > 75
ORDER BY AvgPerformance DESC;

-- ------------------------------------------------------------
-- 24.3 Salary Range by Department
-- Spread between the lowest and highest salary in each dept.
-- (No ORDER BY in the source case study, so row order is not
--  guaranteed; add `ORDER BY SalaryRange DESC` if you need it.)
-- ------------------------------------------------------------
SELECT Department,
       MIN(Salary)               AS LowestSalary,
       MAX(Salary)               AS HighestSalary,
       MAX(Salary) - MIN(Salary) AS SalaryRange
FROM Employees
GROUP BY Department;
