DECLARE @Databasename NVARCHAR(50) = 'HREmployeeDB'

IF NOT EXISTS(SELECT 1 FROM SYS.databases WHERE NAME = @Databasename)

BEGIN
	DECLARE @SQL NVARCHAR(MAX) = 'CREATE DATABASE '+ QUOTENAME(@Databasename)
	EXEC sp_executesql @SQL;
END

USE HREmployeeDB;

CREATE TABLE [dbo].EmployeeData (
    Attrition VARCHAR(20) NOT NULL,
    BusinessTravel VARCHAR(26) NOT NULL,
    CF_age_band VARCHAR(20) NOT NULL,
    CF_attrition_label VARCHAR(35) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    EducationField VARCHAR(50) NOT NULL,
    emp_no VARCHAR(20) PRIMARY KEY,
    EmployeeNumber INT NOT NULL,
    Gender VARCHAR(6) NOT NULL,
    JobRole VARCHAR(50) NOT NULL,
    MaritalStatus VARCHAR(10) NOT NULL,
    OverTime VARCHAR(3) NOT NULL,
    Over18 VARCHAR(3) NOT NULL,
    TrainingTimesLastYear INT NOT NULL,
    Age INT NOT NULL,
    CF_current VARCHAR(3) NOT NULL,
    DailyRate INT NOT NULL,
    DistanceFromHome INT NOT NULL,
    Education VARCHAR(20) NOT NULL,
    EmployeeCount INT NOT NULL,
    EnvironmentSatisfaction INT NOT NULL,
    HourlyRate INT NOT NULL,
    JobInvolvement INT NOT NULL,
    JobLevel INT NOT NULL,
    JobSatisfaction INT NOT NULL,
    MonthlyIncome INT NOT NULL,
    MonthlyRate INT NOT NULL,
    NumCompaniesWorked INT NOT NULL,
    PercentSalaryHike INT NOT NULL,
    PerformanceRating INT NOT NULL,
    RelationshipSatisfaction INT NOT NULL,
    StandardHours INT NOT NULL,
    StockOptionLevel INT NOT NULL,
    TotalWorkingYears INT NOT NULL,
    WorkLifeBalance INT NOT NULL,
    YearsAtCompany INT NOT NULL,
    YearsInCurrentRole INT NOT NULL,
    YearsSinceLastPromotion INT NOT NULL,
    YearsWithCurrentManager INT NOT NULL
);

BULK INSERT EmployeeData
FROM 'D:/HR Employee.csv'
WITH(
    FIELDTERMINATOR = ',',	-- Field terminated by '|',';','\t'
    ROWTERMINATOR = '0x0a', -- Carriage & New Line Character'\r\n','\n','0x0a'(line feed)
    FIRSTROW = 2
);

SELECT TOP(5)* 
FROM EmployeeData

--a) Return the shape of the table
SELECT COUNT(*) AS ROW_SIZE
FROM EmployeeData
SELECT COUNT(*) AS COL_SIZE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'EmployeeData'

--b) Calculate the cumulative sum of total working years for each department
SELECT Department,TotalWorkingYears,
SUM(TotalWorkingYears) OVER(PARTITION BY Department 
ORDER BY TotalWorkingYears ROWS BETWEEN UNBOUNDED PRECEDING
AND CURRENT ROW) AS TotalWorkYrSum
FROM EmployeeData
WHERE TotalWorkingYears > 0

-- c) Which gender have higher strength as workforce in each department
SELECT Department,Gender,Gender_count FROM
(SELECT Department,Gender,COUNT(*) AS Gender_count,
RANK() OVER(PARTITION BY Department ORDER BY COUNT(*) DESC)
AS Gender_rank
FROM EmployeeData
GROUP BY Department,Gender) _
WHERE Gender_rank = 1

--d) Create a new column AGE_BAND and Show Distribution of Employee's Age band group
ALTER TABLE EmployeeData
ADD AGE_BAND_COUNT INT;

UPDATE EmployeeData
SET AGE_BAND_COUNT = (
    SELECT COUNT(*)
    FROM EmployeeData AS ed2
    WHERE ed2.CF_age_band = EmployeeData.CF_age_band
)
SELECT CF_age_band, COUNT(*) as AGE_BAND_COUNT
FROM EmployeeData
GROUP BY CF_age_band

--e) Compare all marital status of employee and find the most frequent marital status
SELECT TOP(1) MaritalStatus,COUNT(*) AS Marital_count
FROM EmployeeData
GROUP BY MaritalStatus
ORDER BY Marital_count DESC

--f) Show the Job Role with Highest Attrition Rate (Percentage)
SELECT TOP(1) JobRole, 
total_yes * 100/total_count AS Attrition_percent
FROM (
	SELECT JobRole,
	COUNT(CASE
		WHEN Attrition = 'Yes' THEN 1
	END) AS total_yes,
	COUNT(*) total_count
	FROM EmployeeData
	GROUP BY JobRole
) _
ORDER BY Attrition_percent DESC

--g) Show distribution of Employee's Promotion,
--Find the maximum chances of employee getting promoted.
SELECT *
FROM EmployeeData

SELECT JobRole,PerformanceRating,YearsInCurrentRole,YearsAtCompany,YearsSinceLastPromotion,
	JobInvolvement,TrainingTimesLastYear
FROM EmployeeData
GROUP BY Attrition,JobRole,PerformanceRating,YearsSinceLastPromotion,
	YearsInCurrentRole,YearsAtCompany,JobInvolvement,TrainingTimesLastYear
ORDER BY YearsAtCompany


--i) Find the rank of employees within each department based on their monthly income
SELECT emp_no, Department,MonthlyIncome,
DENSE_RANK() OVER(PARTITION BY Department ORDER BY MonthlyIncome DESC)
AS Income_rank
FROM EmployeeData

--j) Calculate the running total of 'Total Working Years' for each employee within each 
--department and age band.
SELECT Department,CF_age_band,TotalWorkingYears,
SUM(TotalWorkingYears) OVER(PARTITION BY Department,CF_age_band
ORDER BY TotalWorkingYears ROWS BETWEEN UNBOUNDED PRECEDING
AND CURRENT ROW) AS TotalWorkYrSum
FROM EmployeeData
WHERE TotalWorkingYears > 0

--k) Foreach employee who left, calculate the number of years they worked before leaving and 
--compare it with the average years worked by employees in the same department.
SELECT emp_no, dept.Department, YearsAtCompany, avg_years_in_dept
FROM EmployeeData LEFT JOIN 
(
	SELECT Department, AVG(YearsAtCompany) as avg_years_in_dept
	FROM EmployeeData
	GROUP BY Department
) as dept 
ON dept.Department = EmployeeData.Department
ORDER BY emp_no

--l) Rank the departments by the average monthly income of employees who have left.
SELECT Department,AvgMonthlyIncome,
RANK() OVER(ORDER BY AvgMonthlyIncome DESC)
AS Avg_income_rank
FROM (
	SELECT Department,avg(MonthlyIncome) AvgMonthlyIncome
	FROM EmployeeData
	WHERE Attrition = 'Yes'
	GROUP BY Department
) AS _

--m) Find the if there is any relation between Attrition Rate and Marital Status of Employee.
SELECT MaritalStatus,Attrition,COUNT(*) as marital_count
FROM EmployeeData
GROUP BY  MaritalStatus,Attrition
ORDER BY marital_count DESC
--INSIGHTS : MAJORITY OF EMPLOYEES WHO ARE CURRENTLY WORKING IN THE COMPANY ARE MARRIED AND 
--			 MAJORITY OF EMOPLOYEES WHO LEFT THE COMPANY ARE SINGLE.

--n) Show the Department with Highest Attrition Rate (Percentage)
SELECT TOP(1) Department, 
(COUNT(CASE
	WHEN Attrition = 'Yes' THEN 1
END) * 100 ) / COUNT(*) AS dept_yes_percent
FROM EmployeeData
GROUP BY Department
ORDER BY dept_yes_percent DESC

-- o) Calculate the moving average of monthly income over the past 3 employees for each job role.
SELECT emp_no,MonthlyIncome,
AVG(MonthlyIncome) OVER(ORDER BY MonthlyIncome ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
AS Moving_average_income
FROM EmployeeData

-- p) Identify employees with outliers in monthly income within each job role. [ Condition : 
--Monthly_Income < Q1 - (Q3 - Q1) * 1.5 OR Monthly_Income > Q3 + (Q3 - Q1) ]
SELECT JobRole, MonthlyIncome
FROM(
	SELECT JobRole,MonthlyIncome,
	PERCENTILE_CONT(.25) WITHIN GROUP(ORDER BY MonthlyIncome) OVER(PARTITION BY JobRole)
	AS Q1,
	PERCENTILE_CONT(.5) WITHIN GROUP(ORDER BY MonthlyIncome) OVER(PARTITION BY JobRole) 
	AS Q2,
	PERCENTILE_CONT(.75) WITHIN GROUP(ORDER BY MonthlyIncome) OVER(PARTITION BY JobRole) 
	AS Q3
	FROM EmployeeData
) _
WHERE MonthlyIncome < Q1 - ((Q3 - Q1) * 1.5) OR MonthlyIncome > Q3 + (1.5 * (Q3 - Q1))

-- q) Gender distribution within each job role, show each job role with its gender domination. 
--[Male_Domination or Female_Domination]
SELECT JobRole,Gender
FROM (
	SELECT JobRole,Gender,
	RANK() OVER(PARTITION BY JobRole ORDER BY COUNT(*) DESC)
	AS gender_rank
	FROM EmployeeData
	GROUP BY JobRole,Gender
) AS _
WHERE gender_rank = 1

--r) Percent rank of employees based on training times last year
SELECT emp_no,TrainingTimesLastYear,
PERCENT_RANK() OVER(ORDER BY TrainingTimesLastYear)
AS training_percentage
FROM EmployeeData
ORDER BY training_percentage DESC

--s) Divide employees into 5 groups based on training times last year [Use NTILE ()]
SELECT emp_no,TrainingTimesLastYear,
NTILE(5) OVER(ORDER BY TrainingTimesLastYear)
AS training_tile
FROM EmployeeData

--t) Categorize employees based on training times last year as - Frequent Trainee, Moderate 
--Trainee, Infrequent Trainee
SELECT emp_no,TrainingTimesLastYear,
CASE
	WHEN TrainingTimesLastYear > 4 THEN 'Frequent Trainee'
	WHEN TrainingTimesLastYear > 2 THEN 'Moderate Trainee'
	ELSE 'Infrequent Trainee'
END AS 'Training Frequency'
FROM EmployeeData
ORDER BY TrainingTimesLastYear DESC

--u) Categorize employees as 'High', 'Medium', or 'Low' performers based on their performance 
--rating, using a CASE WHEN statement.
SELECT emp_no,PerformanceRating,
CASE
	WHEN PerformanceRating > 3 THEN 'High Performer'
	WHEN PerformanceRating > 1 THEN 'Medium Performer'
	ELSE 'Low Performer'
END AS 'Performance Ranking'
FROM EmployeeData
ORDER BY PerformanceRating DESC

--v) Use a CASE WHEN statement to categorize employees into 'Poor', 'Fair', 'Good', or 'Excellent' 
--work-life balance based on their work-life balance score.

SELECT emp_no,WorkLifeBalance,
CASE
	WHEN WorkLifeBalance > 3 THEN 'Excellent WorkLifeBalance'
	WHEN WorkLifeBalance > 1 THEN 'Fair WorkLifeBalance'
	ELSE 'Poor WorkLifeBalance'
END AS 'WorkLifeBalance Ranking'
FROM EmployeeData
ORDER BY PerformanceRating DESC


--w) Group employees into 3 groups based on their stock option level using the [NTILE] function.
SELECT StockOptionLevel,
NTILE(3) OVER(ORDER BY StockOptionLevel DESC)
AS 'Stock RANK'
FROM EmployeeData

--x) Find key reasons for Attrition in Company
SELECT JobRole,Department,
AVG(YearsAtCompany) Company_year_Count,
AVG(YearsSinceLastPromotion) year_since_promotion_Count,
AVG(WorkLifeBalance) worklife_avg,
AVG(PercentSalaryHike) hike_percent,
AVG(MonthlyIncome) income_avg,
AVG(EnvironmentSatisfaction) env_satisfaction,
COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) Attrition_rate,
COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END)*100/ COUNT(*) Attrition_percent

FROM EmployeeData
GROUP BY JobRole,Department
ORDER BY Attrition_percent DESC
