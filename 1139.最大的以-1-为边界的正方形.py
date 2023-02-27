#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
# https://leetcode.cn/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (49.50%)
# Likes:    186
# Dislikes: 0
# Total Accepted:    25.1K
# Total Submissions: 45.7K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回
# 0。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 
# 
# 示例 2：
# 
# 输入：grid = [[1,1,0,0]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rs = [list(accumulate(row, initial=0)) for row in grid]  # 每行的前缀和
        cs = [list(accumulate(col, initial=0)) for col in zip(*grid)]  # 每列的前缀和
        for d in range(min(m, n), 0, -1):  # 从大到小枚举正方形边长 d
            for i in range(m - d + 1):
                for j in range(n - d + 1):  # 枚举正方形左上角坐标 (i,j)
                    # 上 左 下 右 四条边 1 的个数均为 d
                    if rs[i][j + d] - rs[i][j] == d and \
                       cs[j][i + d] - cs[j][i] == d and \
                       rs[i + d - 1][j + d] - rs[i + d - 1][j] == d and \
                       cs[j + d - 1][i + d] - cs[j + d - 1][i] == d:
                        return d * d
        return 0
# @lc code=end

