CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
      DECLARE nth_highest_salary INT;
IF (SELECT COUNT(DISTINCT Salary) FROM Employee) < N or N < 0 THEN
        RETURN NULL;
    END IF;
 

    SELECT MIN(Salary) INTO nth_highest_salary
    FROM (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT N
    ) AS subquery;

    RETURN nth_highest_salary;
END