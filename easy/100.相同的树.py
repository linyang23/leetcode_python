#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:   #若都为空，则相同     #迭代结束的标志就是return了值，这里不会出现未return而迭代已结束
            return True
        if not p or not q:    #若p和q只有一个为空，则不同
            return False
        if p.val != q.val:      #若节点值不同，则不同
            return False
        return (self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))
# @lc code=end

