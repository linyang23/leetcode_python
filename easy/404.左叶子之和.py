#
# @lc app=leetcode.cn id=404 lang=python
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sum_1(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            self.n += root.left.val
        self.sum_1(root.left)
        self.sum_1(root.right)
        return self.n

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 这道题对我来说最卡人的是n在递归中会重复赋初始值，所以写成了两个函数
        # ，主函数对分函数进行调用，为了防止因为n为局部变量而主函数定义对子函
        # 数无效，于是通过self来使n处于全局模式
        self.n = 0
        return self.sum_1(root)
# @lc code=end
