SELECT AVG(age) AS average_age
FROM users;

SELECT country, COUNT(*) AS user_count
FROM users
GROUP BY country;

SELECT * 
FROM users
WHERE balance = (
  SELECT MAX(balance)
  FROM users
)
LIMIT 1;

SELECT country, AVG(balance) AS avg_balance
FROM users
GROUP BY country;

SELECT MAX(balance) - MIN(balance) AS balance_diffrence
FROM users;
