--
-- @lc app=leetcode.cn id=180 lang=mysql
--
-- [180] 连续出现的数字
--
-- https://leetcode.cn/problems/consecutive-numbers/description/
--
-- database
-- Medium (48.03%)
-- Likes:    693
-- Dislikes: 0
-- Total Accepted:    137.1K
-- Total Submissions: 285.5K
-- Testcase Example:  '{"headers": {"Logs": ["id", "num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}'
--
-- 表：Logs
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- id 是这个表的主键。
-- 
-- 
-- 
-- 编写一个 SQL 查询，查找所有至少连续出现三次的数字。
-- 
-- 返回的结果表中的数据可以按 任意顺序 排列。
-- 
-- 查询结果格式如下面的例子所示：
-- 
-- 
-- 
-- 示例 1:
-- 
-- 
-- 输入：
-- Logs 表：
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- 输出：
-- Result 表：
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- 解释：1 是唯一连续出现至少三次的数字。
-- 
--
-- @lc code=start
-- 题解: https://leetcode.cn/problems/consecutive-numbers/solutions/21537/sql-server-jie-fa-by-neilsons/
WITH Sub as (
    SELECT
        Id,
        Num,
        row_number() over(
            order by
                id
        ) - ROW_NUMBER() over(
            partition by Num
            order by
                Id
        ) as SerialNumberSubGroup
    FROM
        Logs
),
Result as (
    SELECT
        Num,
        COUNT(1) as SerialCount
    FROM
        Sub
    GROUP BY
        Num,
        SerialNumberSubGroup
    HAVING
        COUNT(1) >= 3
)
SELECT
    DISTINCT Num as ConsecutiveNums
FROM
    Result;

-- @lc code=end