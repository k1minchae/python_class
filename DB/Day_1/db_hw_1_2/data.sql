-- 모든 데이터 조회
SELECT * FROM tracks;

-- Name , Milliseconds, UnitPrice 열의 모든 데이터 조회
SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;

-- GenreId 행의 값이 1인 모든 데이터 조회
SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1;

-- 모든 데이터를 name 기준으로 오름차순 정렬조회
SELECT
  *
FROM
  tracks
ORDER BY
  name;
-- track 테이블의 모든 데이터를 조회하되 10개만출력
SELECT
  *
FROM
  tracks
LIMIT 10;