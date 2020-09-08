#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #中序遍历
        global res, prev
        res = float("inf")
        prev = float("-inf")
        def mid(root):
            #声明非局部变量，从而在外部定义，避免函数内重复定义的问题
            global res, prev
            if not root:
                return
            mid(root.left)
            res = min(res, root.val - prev)
            prev = root.val
            mid(root.right)
        mid(root)
        return res
# @lc code=end

