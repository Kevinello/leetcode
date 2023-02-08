#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#

# @lc code=start
from typing import List
from collections import defaultdict


# 字典树
class DictTree:

    def __init__(self):
        self.children = dict()
        # 标注为path的尾节点，-1表示为中间节点
        self.ref = -1


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = DictTree()
        for i, path in enumerate(folder):
            cur = root
            for name in path.split("/")[1:]:
                if name not in cur.children:
                    cur.children[name] = DictTree()
                cur = cur.children[name]
            # 记录尾节点（同时也是原folder列表中的下标）
            cur.ref = i

        non_sub_paths = []

        def dfs(cur: DictTree):
            # 从根节点dfs找到第一个尾节点就加入结果集，并返回（第一个尾节点的子节点都为子目录）
            if cur.ref >= 0:
                non_sub_paths.append(folder[cur.ref])
                return
            for child in cur.children.values():
                dfs(child)

        dfs(root)
        return non_sub_paths


# @lc code=end
