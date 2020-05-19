#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0            #空节点不加深度
        else:
            left_height = self.maxDepth(root.left)      #递归穷举所有的路径
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1      #每经过一个非空节点则深度+1，max用于选出最深的路径
# @lc code=end

