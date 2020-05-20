#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:        #空二叉树最小深度为0
            return 0
        if not root.left:       #左节点为空，继续往右遍历
            return 1 + self.minDepth(root.right)
        if not root.right:      #右节点为空，继续往左遍历
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))     #左右节点均不空，则递归获取最小的；左右节点均为空，则只加根节点，此处探索结束
# @lc code=end

