#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#

# @lc code=start
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_consecutive = 0
        for num in coins:
            if num <= max_consecutive+1:
                max_consecutive += num
            else:
                break
        return max_consecutive+1
# @lc code=end

