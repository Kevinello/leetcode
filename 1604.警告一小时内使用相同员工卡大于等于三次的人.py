#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        record = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour = int(time[:2])
            minute = int(time[3:])
            all_in_min = hour * 60 + minute
            record[name].append(all_in_min)

        alert_list = []
        for name, times in record.items():
            times.sort()
            # 
            if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
                alert_list.append(name)
        alert_list.sort()
        return alert_list
# @lc code=end

