-- name 의 값이 love 글자를 포함한 데이터 조회
SELECT name
FROM tracks
WHERE name LIKE '%love%';

-- GenreID 의 값이 1이고 Milliseconds 의 값이 300000 이상인 데이터 모두 조회 + UnitPrice 기준 내림차순 정렬

-- GenreID 별로 그룹화, GenreID 와 각 그룹별 데이터의 수 조회, 단 그룹별 데이터 수는 TotalTracks 필드로 표기해서 나타내시오

-- GenreID 별로 그룹화, 각 그룹별 UnitPrice의 총합을 계산해서 조회, 단 UnitPrice 의 총합은 TotalPrice로 표기, 그중 TotalPrice의 값이 100 이상인 데이터들만 조회