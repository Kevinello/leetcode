#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#

# @lc code=start
from typing import List

class Solution:

    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for line_number in range(len(grid)):
            if grid[line_number][line_number] == 0 or grid[line_number][-line_number - 1] == 0:
                return False
            if len(grid) % 2 == 1 and line_number == int(len(grid) / 2):
                if sum(grid[line_number]) != grid[line_number][line_number]:
                    return False
            elif sum(grid[line_number]) != grid[line_number][line_number] + grid[line_number][-line_number - 1]:
                return False
        return True