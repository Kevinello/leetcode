with result as (
    SELECT
        salary as shs
    FROM
        Employee
    GROUP BY
        salary
    ORDER BY
        salary DESC
    LIMIT
        1 OFFSET 1
)
select
    IFNULL((SELECT shs FROM result), NULL) as SecondHighestSalary;