-- ================================
-- WINDOWS FUNCTION
-- ================================
SELECT gender, AVG(salary) as avg_salary
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
;

-- ================================
-- SUBQUERYS
-- ================================
SELECT 
    AVG(max_age)
FROM
    (SELECT 
        gender, 
        AVG(age) as avg_age, 
        MAX(age) as max_age, 
        MIN(age) as min_age, 
        COUNT(age)
    FROM
        employee_demographics
    GROUP BY gender) AS agg_table;

SELECT gender, MAX(age) AS max, MIN(age) AS min, COUNT(age)
FROM employee_demographics
GROUP BY gender;

SELECT 
    first_name,
    salary,
    (SELECT 
            AVG(salary)
        FROM
            employee_salary)
FROM
    employee_salary;
SELECT 
    *
FROM
    employee_demographics
WHERE
    employee_id IN (SELECT 
            employee_id
        FROM
            employee_salary
        WHERE
            dept_id = 1)
;
SELECT * FROM employee_salary;
SELECT * FROM parks_departments;

-- ================================
-- CASE STATEMENTS
-- ================================
-- Pays Increase and bonus
SELECT 
	first_name, 
	last_name,
    salary,
CASE
	WHEN salary < 50000 THEN salary * 1.05
    WHEN salary > 50000 THEN salary * 1.07
END AS new_salary,
CASE
	WHEN dept_id = 6 THEN salary * .10
END AS bonus
FROM employee_salary;

SELECT
	first_name,
    last_name,
    age,
CASE
	WHEN age <=30 THEN 'Young'
    WHEN age BETWEEN 30 AND 50 THEN 'Old'
    WHEN age >=50 THEN "On Death's Door"
END AS Age_Bracket
FROM employee_demographics;

-- ================================
-- STRING FUNCTION'S
-- ================================
SELECT 
first_name,
last_name,
CONCAT(first_name,' ',last_name) AS full_name
FROM employee_demographics;

SELECT 
first_name,
LOCATE(first_name,'Ann')
FROM employee_demographics;

SELECT 
first_name,
REPLACE(first_name,'a','z')
FROM employee_demographics;

SELECT first_name, LEFT(first_name, 4),RIGHT(first_name, 4),
substring(first_name,3,2),
birth_date,
SUBSTRING(birth_date,6,2)
FROM employee_demographics;

SELECT RTRIM( '        sky     ') ;

SELECT first_name, length(first_name)
FROM employee_demographics
ORDER BY 2
;
-- ================================
-- UNIONS
-- ================================
SELECT first_name, last_name, 'Old Men' AS Label
FROM employee_demographics
WHERE age > 40 AND gender = 'Male'
UNION
SELECT first_name, last_name, 'Old Lady' AS Label
FROM employee_demographics
WHERE age > 40 AND gender = 'Female'
UNION
SELECT first_name, last_name, 'Highly Paid Employee' AS Label
FROM employee_salary
WHERE salary > 70000
ORDER BY first_name,last_name
;

SELECT first_name, last_name
FROM employee_demographics
UNION ALL
SELECT first_name, last_name
FROM employee_salary
;

-- ================================
-- JOINS
-- ================================
-- Join multiple table together

SELECT *
FROM employee_demographics AS dem
INNER JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
INNER JOIN parks_departments AS pd
	ON sal.dept_id = pd.department_id;

-- Join selfs
SELECT
	emp1.employee_id as emp_santa,
	emp1.first_name as first_name_santa,
    emp1.last_name as last_name_santa,
    emp2.employee_id as emp_name,
    emp2.first_name as first_name_emp,
    emp2.last_name as last_name_emp
FROM 
	employee_salary AS emp1
INNER JOIN employee_salary AS emp2
	ON emp1.employee_id +1 = emp2.employee_id
;

SELECT
	dem.employee_id,
    age,
    occupation
FROM 
	employee_demographics AS dem
RIGHT JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id
;

-- ================================
-- LIMIT AND ALIASING
-- ================================
SELECT
	*
FROM 
	employee_demographics
ORDER BY age DESC
LIMIT 1,1
;

-- ================================
-- HAVING AND WHERE
-- ================================
SELECT
	occupation,
    AVG(salary) as MEDIA_SALARIAL -- apelido para melhor governança
FROM 
	employee_salary
WHERE occupation LIKE '%manager%'
GROUP BY occupation
HAVING AVG(salary) > 7500
;

-- ================================
-- ORDER BY
-- ================================
SELECT
	*
FROM 
	employee_demographics
ORDER BY gender, age;
;
-- ================================
-- GROUP BY
-- ================================
SELECT
	gender,
    AVG(age),
    MIN(age),
    MAX(age),
    COUNT(age)
FROM 
	employee_demographics
GROUP BY
	gender 
;

-- ================================
-- LIKE STATEMENT
-- ================================
SELECT
	*
FROM 
	employee_demographics
WHERE
	first_name LIKE 'a___%'
;

SELECT
	*
FROM 
	employee_demographics
WHERE
	first_name LIKE 'Jer%'
;

-- ================================
-- WHERE CLOUSE
-- ================================
SELECT
	*
FROM 
	employee_demographics
WHERE
	birth_date > '1985-01-01'
OR NOT
	gender != 'Female'
;

-- AND OR NOT == Logical Operators
SELECT
	*
FROM 
	employee_demographics
WHERE
	gender != 'Female'
;

SELECT
	*
FROM 
	employee_salary
WHERE
	salary <= 50000
;


SELECT
	*
FROM 
	employee_demographics
WHERE
	first_name = 'Leslie'
;
-- ================================
-- SELECT'S 
-- PEMDAS - Order operations math
-- Parenteses, Exponent, Multiply, Division, Adiction and Subtraction
-- ================================
SELECT DISTINCT
	first_name,
    gender
FROM 
	employee_demographics;

SELECT 
	first_name,
	last_name,
	birth_date,
    age,
    (age + 10) * 10
FROM 
	employee_demographics;

SELECT 
	*
FROM 
	employee_salary;

-- ================================
-- CHOOSE WHAT DATABASE USES
-- ================================
USE parks_and_recreation;