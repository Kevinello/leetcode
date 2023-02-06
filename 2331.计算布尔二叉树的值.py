#
# @lc app=leetcode.cn id=2331 lang=python3
#
# [2331] 计算布尔二叉树的值
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def evaluateTree(self, root: TreeNode) -> bool:

        def cal_sub_tree(root: TreeNode) -> bool:
            if root.val == 2:
                return cal_sub_tree(root.left) or cal_sub_tree(root.right)
            elif root.val == 3:
                return cal_sub_tree(root.left) and cal_sub_tree(root.right)
            else:
                return root.val == 1

        return cal_sub_tree(root)
# @lc code=end
