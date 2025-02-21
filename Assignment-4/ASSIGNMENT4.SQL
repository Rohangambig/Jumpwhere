DEPARTMENT TABLE
+----+------------+-----------+
| NO | NAME       | LOCATION  |
+----+------------+-----------+
| 10 | ACCOUNTS   | BANGALORE |
| 20 | IT         | DELHI     |
| 30 | PRODUCTION | CHENNAI   |
| 40 | SALES      | HYDERABAD |
| 50 | ADMIN      | LONDON    |
+----+------------+-----------+


EMPLOYEE TABLE 
+------+----------+--------+------------+-----------+---------+---------+
| NO   | NAME     | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+----------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN   |  19000 | 1980-01-01 |      2100 |      20 |    1003 |
| 1002 | KAPIL    |  15000 | 1970-01-01 |      2300 |      10 |    1003 |
| 1003 | STEFEN   |  12000 | 2001-01-01 |       500 |      20 |    1007 |
| 1004 | WILLIAMS |   9000 | 1990-01-01 |      NULL |      30 |    1007 |
| 1005 | JOHN     |   5000 | 2005-01-01 |      NULL |      30 |    1006 |
| 1006 | DRAVID   |  19000 | 1985-01-01 |      2400 |      10 |    1007 |
| 1007 | MARTIN   |  21000 | 2000-01-01 |      1040 |    NULL |    NULL |
+------+----------+--------+------------+-----------+---------+---------+



1.  Select employee details  of dept number 10 or 30
SELECT * FROM EMPLOYEE WHERE DEPT_NO = 10 OR DEPT_NO = 30;


+------+----------+--------+------------+-----------+---------+---------+
| NO   | NAME     | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+----------+--------+------------+-----------+---------+---------+
| 1002 | KAPIL    |  15000 | 1970-01-01 |      2300 |      10 |    1003 |
| 1006 | DRAVID   |  19000 | 1985-01-01 |      2400 |      10 |    1007 |
| 1004 | WILLIAMS |   9000 | 1990-01-01 |      NULL |      30 |    1007 |
| 1005 | JOHN     |   5000 | 2005-01-01 |      NULL |      30 |    1006 |
+------+----------+--------+------------+-----------+---------+---------+



2. Write a query to fetch all the dept details with more than 1 Employee.
 SELECT DEPT_NO  , COUNT(NO) AS EMPLOYEES FROM EMPLOYEE GROUP BY DEPT_NO HAVING COUNT(DEPT_NO) > 1;

+---------+-----------+
| DEPT_NO | EMPLOYEES |
+---------+-----------+
|      10 |         2 |
|      20 |         2 |
|      30 |         2 |
+---------+-----------+


3. Write a query to fetch employee details whose name starts with the letter “S”
 SELECT * FROM EMPLOYEE WHERE NAME  LIKE "S%";

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN |  19000 | 1980-01-01 |      2100 |      20 |    1003 |
| 1003 | STEFEN |  12000 | 2001-01-01 |       500 |      20 |    1007 |
+------+--------+--------+------------+-----------+---------+---------+



4.Select Emp Details Whose experience is more than 2 years
SELECT * FROM EMPLOYEE WHERE DATEDIFF(CURDATE(),HIRE_DATE) / 365 > 2;


+------+----------+--------+------------+-----------+---------+---------+
| NO   | NAME     | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+----------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN   |  19000 | 1980-01-01 |      2100 |      20 |    1003 |
| 1002 | KAPIL    |  15000 | 1970-01-01 |      2300 |      10 |    1003 |
| 1003 | STEFEN   |  12000 | 2001-01-01 |       500 |      20 |    1007 |
| 1004 | WILLIAMS |   9000 | 1990-01-01 |      NULL |      30 |    1007 |
| 1005 | JOHN     |   5000 | 2005-01-01 |      NULL |      30 |    1006 |
| 1006 | DRAVID   |  19000 | 1985-01-01 |      2400 |      10 |    1007 |
| 1007 | MARTIN   |  21000 | 2000-01-01 |      1040 |    NULL |    NULL |
+------+----------+--------+------------+-----------+---------+---------+



5. Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)

 SELECT REPLACE("SACHIN","A","#") AS REPLACE_NAME;

+--------------+
| REPLACE_NAME |
+--------------+
| S#CHIN       |
+--------------+


6. Write a query to fetch employee name and his/her manager name. 

 SELECT E1.NAME AS EMPLOYEE, E2.NAME AS MANAGER FROM EMPLOYEE AS E1 LEFT JOIN EMPLOYEE E2 ON E1.MANAGER = E2.NO;

+----------+---------+
| EMPLOYEE | MANAGER |
+----------+---------+
| SACHIN   | STEFEN  |
| KAPIL    | STEFEN  |
| STEFEN   | MARTIN  |
| WILLIAMS | MARTIN  |
| JOHN     | DRAVID  |
| DRAVID   | MARTIN  |
| MARTIN   | NULL    |
+----------+---------+


7. Fetch Dept Name , Total Salry of the Dept

 SELECT D.NAME , SUM(E.SALARY) FROM DEPT AS D JOIN EMPLOYEE AS E ON E.DEPT_NO = D.NO GROUP BY D.NAME;


+------------+---------------+
| NAME       | SUM(E.SALARY) |
+------------+---------------+
| IT         |         31000 |
| ACCOUNTS   |         34000 |
| PRODUCTION |         14000 |
+------------+---------------+


8. Write a query to fetch ALL the  employee details along with department name, department location, irrespective of employee existance in the department.

 SELECT E.NO,E.NAME AS EMP_NAME,D.NAME AS DEPT_NAME,E.HIRE_DATE ,D.LOCATION FROM DEPT AS D RIGHT JOIN EMPLOYEE AS E ON E.DEPT_NO = D.NO;


+------+----------+------------+------------+-----------+
| NO   | EMP_NAME | DEPT_NAME  | HIRE_DATE  | LOCATION  |
+------+----------+------------+------------+-----------+
| 1001 | SACHIN   | IT         | 1980-01-01 | DELHI     |
| 1002 | KAPIL    | ACCOUNTS   | 1970-01-01 | BANGALORE |
| 1003 | STEFEN   | IT         | 2001-01-01 | DELHI     |
| 1004 | WILLIAMS | PRODUCTION | 1990-01-01 | CHENNAI   |
| 1005 | JOHN     | PRODUCTION | 2005-01-01 | CHENNAI   |
| 1006 | DRAVID   | ACCOUNTS   | 1985-01-01 | BANGALORE |
| 1007 | MARTIN   | NULL       | 2000-01-01 | NULL      |
+------+----------+------------+------------+-----------+


9. Write an update statement to increase the employee salary by 10 %

 UPDATE EMPLOYEE SET SALARY = SALARY + ( ( SALARY * 10 ) / 100  )

+------+----------+--------+------------+-----------+---------+---------+
| NO   | NAME     | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+----------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN   |  20900 | 1980-01-01 |      2100 |      20 |    1003 |
| 1002 | KAPIL    |  16500 | 1970-01-01 |      2300 |      10 |    1003 |
| 1003 | STEFEN   |  13200 | 2001-01-01 |       500 |      20 |    1007 |
| 1004 | WILLIAMS |   9900 | 1990-01-01 |      NULL |      30 |    1007 |
| 1005 | JOHN     |   5500 | 2005-01-01 |      NULL |      30 |    1006 |
| 1006 | DRAVID   |  20900 | 1985-01-01 |      2400 |      10 |    1007 |
| 1007 | MARTIN   |  23100 | 2000-01-01 |      1040 |    NULL |    NULL |
+------+----------+--------+------------+-----------+---------+---------+


10.Write a statement to delete employees belong to Chennai location.

DELETE FROM EMPLOYEE AS E WHERE E.DEPT_NO = ( SELECT D.NO FROM DEPT AS D WHERE D.LOCATION = "CHENNAI");


+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN |  20900 | 1980-01-01 |      2100 |      20 |    1003 |
| 1002 | KAPIL  |  16500 | 1970-01-01 |      2300 |      10 |    1003 |
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |
| 1006 | DRAVID |  20900 | 1985-01-01 |      2400 |      10 |    1007 |
| 1007 | MARTIN |  23100 | 2000-01-01 |      1040 |    NULL |    NULL |
+------+--------+--------+------------+-----------+---------+---------+


11.Get Employee Name and gross salary (sal + comission) .

SELECT E1.NAME, E1.SALARY + E1.COMMISION AS GROSS_SALARY FROM EMPLOYEE AS E1 WHERE COMMISION IS NOT NULL;

+--------+--------------+
| NAME   | GROSS_SALARY |
+--------+--------------+
| SACHIN |        23000 |
| KAPIL  |        18800 |
| STEFEN |        13700 |
| DRAVID |        23300 |
| MARTIN |        24140 |
+--------+--------------+


12. Increase the data length of the column Ename of Emp table from  100 to 250 using ALTER statement

 ALTER TABLE EMPLOYEE MODIFY NAME VARCHAR(250); 


+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| NO        | int          | NO   | PRI | NULL    |       |
| NAME      | varchar(250) | YES  |     | NULL    |       |
| SALARY    | bigint       | YES  |     | NULL    |       |
| HIRE_DATE | date         | YES  |     | NULL    |       |
| COMMISION | bigint       | YES  |     | NULL    |       |
| DEPT_NO   | int          | YES  | MUL | NULL    |       |
| MANAGER   | int          | YES  | MUL | NULL    |       |
+-----------+--------------+------+-----+---------+-------+


13. Write query to get current datetime

SELECT CURDATE();

+------------+
| CURDATE()  |
+------------+
| 2025-02-20 |
+------------+

14. Write a statement to create STUDENT table, with related 5 columns
CREATE TABLE STUDENT ( ID INT PRIMARY KEY, NAME VARCHAR(20), BATCH INT, CLASS VARCHAR(10), GRADE DECIMAL);

DESC STUDENT;
+-------+---------------+------+-----+---------+-------+
| Field | Type          | Null | Key | Default | Extra |
+-------+---------------+------+-----+---------+-------+
| ID    | int           | NO   | PRI | NULL    |       |
| NAME  | varchar(20)   | YES  |     | NULL    |       |
| BATCH | int           | YES  |     | NULL    |       |
| CLASS | varchar(10)   | YES  |     | NULL    |       |
| GRADE | decimal(10,0) | YES  |     | NULL    |       |
+-------+---------------+------+-----+---------+-------+

15. Write a query to fetch number of employees in who is getting salary more than 15000

SELECT COUNT(*) AS COUNT FROM EMPLOYEE WHERE SALARY > 15000;

+-------+
| COUNT |
+-------+
|     4 |
+-------+

16. Write a query to fetch minimum salary, maximum salary and average salary from emp table

SELECT MIN(SALARY) AS MIN_SALARY,MAX(SALARY) AS MAX_SALARY , AVG(SALARY) AS AVG_SALARY FROM EMPLOYEE;

+------------+------------+------------+
| MIN_SALARY | MAX_SALARY | AVG_SALARY |
+------------+------------+------------+
|      13200 |      23100 | 18920.0000 |
+------------+------------+------------+

17. Write a query to fetch number of employees in each location.

SELECT D.LOCATION , COUNT(E.NO) FROM EMPLOYEE AS E LEFT JOIN DEPT AS D ON E.DEPT_NO = D.NO WHERE LOCATION IS NOT NULL GROUP BY D.LOCATION;

+-----------+-------------+
| LOCATION  | COUNT(E.NO) |
+-----------+-------------+
| BANGALORE |           2 |
| DELHI     |           2 |
+-----------+-------------+

18. Write a query to display emplyee names in descending order

SELECT NAME FROM EMPLOYEE ORDER BY NAME DESC;


+--------+
| NAME   |
+--------+
| STEFEN |
| SACHIN |
| MARTIN |
| KAPIL  |
| DRAVID |
+--------+

19. Write a statement to create a new table(EMP_BKP) from the existing EMP table 

CREATE TABLE EMP_BKP AS SELECT * FROM EMPLOYEE;

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN |  20900 | 1980-01-01 |      2100 |      20 |    1003 |
| 1002 | KAPIL  |  16500 | 1970-01-01 |      2300 |      10 |    1003 |
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |
| 1006 | DRAVID |  20900 | 1985-01-01 |      2400 |      10 |    1007 |
| 1007 | MARTIN |  23100 | 2000-01-01 |      1040 |    NULL |    NULL |
+------+--------+--------+------------+-----------+---------+---------+


20. Write a query to fetch first 3 characters from employee name appended with salary.

SELECT CONCAT(SUBSTRING(NAME,1,3),SALARY) AS NAME FROM EMPLOYEE;

+------------+
| NEW_STRING |
+------------+
| SAC20900   |
| KAP16500   |
| STE13200   |
| DRA20900   |
| MAR23100   |
+------------+


21. Get the details of the employees whose name starts with S

SELECT * FROM EMPLOYEE WHERE NAME LIKE "S%";

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN |  20900 | 1980-01-01 |      2100 |      20 |    1003 |
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |
+------+--------+--------+------------+-----------+---------+---------+

22.  Get the details of the employees who works in Bangalore location

SELECT E.* FROM EMPLOYEE AS E LEFT JOIN DEPT AS D ON D.NO = E.DEPT_NO WHERE D.LOCATION = "BANGALORE";

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1002 | KAPIL  |  16500 | 1970-01-01 |      2300 |      10 |    1003 |
| 1006 | DRAVID |  20900 | 1985-01-01 |      2400 |      10 |    1007 |
+------+--------+--------+------------+-----------+---------+---------+


23.  Write the query to get the employee details whose name started within  any letter between  A and K.
SELECT * FROM EMPLOYEE WHERE NAME BETWEEN 'A%' AND 'KZ%';

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1002 | KAPIL  |  16500 | 1970-01-01 |      2300 |      10 |    1003 |
| 1006 | DRAVID |  20900 | 1985-01-01 |      2400 |      10 |    1007 |
+------+--------+--------+------------+-----------+---------+---------+


24.  Write a query in SQL to display the employees whose manager name is Stefen 

SELECT E1.* FROM EMPLOYEE AS E1 JOIN EMPLOYEE AS E2 ON E1.MANAGER = E2.NO AND E2.NAME = "STEFEN";

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1001 | SACHIN |  20900 | 1980-01-01 |      2100 |      20 |    1003 |
| 1002 | KAPIL  |  16500 | 1970-01-01 |      2300 |      10 |    1003 |
+------+--------+--------+------------+-----------+---------+---------+

25. Write a query in SQL to list the name of the managers who is having maximum number of employees working under him.

SELECT E2.NAME FROM EMPLOYEE AS E1 JOIN EMPLOYEE AS E2 ON E1.MANAGER = E2.NO GROUP BY E2.NAME HAVING COUNT(E1.NAME) = (SELECT MAX(COUNT) FROM ( SELECT COUNT(E1.NO) AS COUNT FROM EMPLOYEE AS E1 JOIN EMPLOYEE AS E2 ON E1.MANAGER = E2.NO  GROUP BY E2.NO ) AS MANAGERCOUNTS );


+--------+
| NAME   |
+--------+
| STEFEN |
| MARTIN |
+--------+


26. Write a query to display the employee details, department details and the manager details of the employee who has second highest salary

SELECT E.NAME , E.SALARY,D.NO,D.NAME,D.LOCATION,M.NAME AS MANAGER FROM EMPLOYEE AS E JOIN DEPT AS D ON D.NO = E.DEPT_NO JOIN EMPLOYEE AS M ON M.NO = E.MANAGER WHERE E.SALARY = (SELECT SALARY FROM EMPLOYEE  ORDER BY SALARY  LIMIT 1 OFFSET 1);

+-------+--------+----+----------+-----------+---------+
| NAME  | SALARY | NO | NAME     | LOCATION  | MANAGER |
+-------+--------+----+----------+-----------+---------+
| KAPIL |  16500 | 10 | ACCOUNTS | BANGALORE | STEFEN  |
+-------+--------+----+----------+-----------+---------+


27. Write a query to list all details of all the managers.

SELECT DISTINCT E2.* FROM EMPLOYEE AS E1 JOIN EMPLOYEE AS E2 ON E1.MANAGER = E2.NO;

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |
| 1007 | MARTIN |  23100 | 2000-01-01 |      1040 |    NULL |    NULL |
+------+--------+--------+------------+-----------+---------+---------+

28. Write a query to list the details and total experience of all the managers

SELECT DISTINCT E2.*, DATEDIFF(CURDATE(),E2.HIRE_DATE) /  365 AS EXPERIENCE FROM EMPLOYEE AS E1 JOIN EMPLOYEE AS E2 ON E1.MANAGER = E2.NO;

+------+--------+--------+------------+-----------+---------+---------+------------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER | EXPERIENCE |
+------+--------+--------+------------+-----------+---------+---------+------------+
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |    24.1534 |
| 1007 | MARTIN |  23100 | 2000-01-01 |      1040 |    NULL |    NULL |    25.1562 |
+------+--------+--------+------------+-----------+---------+---------+------------+


29. Write a query to list the employees who is manager and  takes commission less than 1000 and works in Delhi.

SELECT DISTINCT E2.* FROM EMPLOYEE AS E1 JOIN EMPLOYEE AS E2 ON E1.MANAGER = E2.NO JOIN DEPT AS D ON D.NO = E2.DEPT_NO WHERE D.LOCATION = "DELHI" AND E2.COMMISION < 1000;

+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |
+------+--------+--------+------------+-----------+---------+---------+

30. Write a query to display the details of employees who are senior to Martin.

SELECT * FROM EMPLOYEE WHERE HIRE_DATE > (SELECT HIRE_DATE FROM EMPLOYEE WHERE NAME = "MARTIN");


+------+--------+--------+------------+-----------+---------+---------+
| NO   | NAME   | SALARY | HIRE_DATE  | COMMISION | DEPT_NO | MANAGER |
+------+--------+--------+------------+-----------+---------+---------+
| 1003 | STEFEN |  13200 | 2001-01-01 |       500 |      20 |    1007 |
+------+--------+--------+------------+-----------+---------+---------+








