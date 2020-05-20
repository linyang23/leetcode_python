#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root: TreeNode) -> bool:       #高度函数，用于返回指定点的高度
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:        #空二叉树为二叉平衡树
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:       #左右节点高度差大于一，则不是二叉平衡树
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)       #从上到下遍历判定是否符合平衡二叉树的规则
# @lc code=end

