-- ============================================================================
-- CityCab — SQL Analysis (Day 9)
-- Table: rides  (the cleaned dataset, loaded via df.to_sql("rides", conn))
-- Each query is labelled with the BUSINESS QUESTION it answers.
-- ============================================================================

-- Q1. BUSINESS QUESTION: "Which city earns the most total fare?"
--     Technique: GROUP BY + SUM + ORDER BY
SELECT City, SUM(Fare) AS TotalFare
FROM rides
GROUP BY City
ORDER BY TotalFare DESC;
-- Result: Mumbai 680 | Pune 660 | Delhi 310


-- Q2. BUSINESS QUESTION: "Which rides cost more than Rs.150?"
--     Technique: WHERE + ORDER BY
SELECT Driver, City, Fare
FROM rides
WHERE Fare > 150
ORDER BY Fare DESC;
-- Result: Sahil 380, Asha 300, Divya 200, Imran 160, Tara 160, Asha 160


-- Q3. BUSINESS QUESTION: "List all rides in Pune."
--     Technique: WHERE filter
SELECT Driver, Distance, Fare
FROM rides
WHERE City = 'Pune';
-- Result: Ravi (5.2 km, 120), Imran (3.5 km, 160), Sahil (15.0 km, 380)
