#
# @lc app=leetcode.cn id=1145 lang=python3
#
# [1145] 二叉树着色游戏
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        x_node = None

        def get_sub_tree_sum(node):
            if not node:
                return 0
            return 1 + get_sub_tree_sum(node.left) + get_sub_tree_sum(node.right)

        # 先BFS找到x
        to_search_node = [root, ]
        while not x_node:
            tmp_to_search_node = []
            for node in to_search_node:
                if not node:
                    continue
                if node.val == x:
                    x_node = node
                    break
                else:
                    tmp_to_search_node.append(node.left)
                    tmp_to_search_node.append(node.right)
            to_search_node = tmp_to_search_node
        
        left_sum = get_sub_tree_sum(x_node.left)
        if left_sum >= (n + 1) // 2:
            return True
        right_sum = get_sub_tree_sum(x_node.right)
        if right_sum >= (n + 1) // 2:
            return True
        father_sum = n - left_sum - right_sum - 1
        return father_sum >= (n + 1) // 2


# @lc code=end
