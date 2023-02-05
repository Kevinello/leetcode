#
# @lc app=leetcode.cn id=1210 lang=python3
#
# [1210] 穿过迷宫的最少移动次数
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # dist存储已走过的路径，保证最短路径
        step_to_pos = {(0, 0, 0): 0}
        # deque: python 预置队列包
        to_search_pos = deque([(0, 0, 0)])

        # 循环实现BFS
        while to_search_pos:
            x, y, status = to_search_pos.popleft()
            # 区分姿态
            if status == 0:
                # 向右移动一个单元格，并判断移动合法性（没有被阻挡）
                if y + 2 < n and (x, y + 1, 0) not in step_to_pos and grid[x][y + 2] == 0:
                    step_to_pos[(x, y + 1, 0)] = step_to_pos[(x, y, 0)] + 1
                    to_search_pos.append((x, y + 1, 0))
                
                # 向下移动一个单元格
                if x + 1 < n and (x + 1, y, 0) not in step_to_pos and grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                    step_to_pos[(x + 1, y, 0)] = step_to_pos[(x, y, 0)] + 1
                    to_search_pos.append((x + 1, y, 0))
                
                # 顺时针旋转 90 度
                if x + 1 < n and y + 1 < n and (x, y, 1) not in step_to_pos and grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                    step_to_pos[(x, y, 1)] = step_to_pos[(x, y, 0)] + 1
                    to_search_pos.append((x, y, 1))
            else:
                # 向右移动一个单元格
                if y + 1 < n and (x, y + 1, 1) not in step_to_pos and grid[x][y + 1] == grid[x + 1][y + 1] == 0:
                    step_to_pos[(x, y + 1, 1)] = step_to_pos[(x, y, 1)] + 1
                    to_search_pos.append((x, y + 1, 1))
                
                # 向下移动一个单元格
                if x + 2 < n and (x + 1, y, 1) not in step_to_pos and grid[x + 2][y] == 0:
                    step_to_pos[(x + 1, y, 1)] = step_to_pos[(x, y, 1)] + 1
                    to_search_pos.append((x + 1, y, 1))
                
                # 逆时针旋转 90 度
                if x + 1 < n and y + 1 < n and (x, y, 0) not in step_to_pos and grid[x][y + 1] == grid[x + 1][y + 1] == 0:
                    step_to_pos[(x, y, 0)] = step_to_pos[(x, y, 1)] + 1
                    to_search_pos.append((x, y, 0))

        return step_to_pos.get((n - 1, n - 2, 0), -1)
# @lc code=end
