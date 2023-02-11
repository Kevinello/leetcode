--
-- @lc app=leetcode.cn id=177 lang=mysql
--
-- [177] 第N高的薪水
--
-- https://leetcode.cn/problems/nth-highest-salary/description/
--
-- database
-- Medium (46.84%)
-- Likes:    680
-- Dislikes: 0
-- Total Accepted:    191.5K
-- Total Submissions: 408.9K
-- Testcase Example:  '{"headers": {"Employee": ["id", "salary"]}, "argument": 2, "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}'
--
-- 表: Employee
-- 
-- 
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- Id是该表的主键列。
-- 该表的每一行都包含有关员工工资的信息。
-- 
-- 
-- 
-- 
-- 编写一个SQL查询来报告 Employee 表中第 n 高的工资。如果没有第 n 个最高工资，查询应该报告为 null 。
-- 
-- 查询结果格式如下所示。
-- 
-- 
-- 
-- 示例 1:
-- 
-- 
-- 输入: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- n = 2
-- 输出: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+
-- 
-- 
-- 示例 2:
-- 
-- 
-- 输入: 
-- Employee 表:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- n = 2
-- 输出: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | null                   |
-- +------------------------+
-- 
--
-- @lc code=start
-- 因为需要在没有数据时返回null，所以必须用子查询
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
  SELECT
    salary
  FROM
    (
      SELECT
        DISTINCT salary,
        dense_rank() over(
          ORDER BY
            salary DESC
        ) AS rnk
      FROM
        employee
    ) tmp
  WHERE
    rnk = N
);

END;

-- @lc code=end