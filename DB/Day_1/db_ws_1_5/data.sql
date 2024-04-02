SELECT * 
FROM users
WHERE age >= 30 AND balance >= 1000;

SELECT *
FROM users
WHERE balance <= 1000 AND age <= 20;

SELECT *
FROM users
WHERE first_name LIKE '현%' AND country = '제주특별자치도' AND 
age = (SELECT MAX(age) FROM users WHERE first_name LIKE '현%' AND country = '제주특별자치도');

SELECT *
FROM users
WHERE last_name = '박' AND 
age = (SELECT MIN(age) FROM users WHERE age >= 25 AND last_name ='박')
LIMIT 1;

SELECT *
FROM users
WHERE first_name = '재은' AND balance = (SELECT MAX(balance) FROM users WHERE first_name = '재은') OR 
first_name = '영일' AND balance = (SELECT MAX(balance) FROM users WHERE first_name = '영일');

SELECT first_name, last_name, age, country, phone, MAX(balance) AS max_balance
FROM users
GROUP BY country
ORDER BY balance DESC, country DESC;