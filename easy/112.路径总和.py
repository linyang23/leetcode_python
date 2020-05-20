#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> list:   
        if not root:        #若根节点为空，则返回False
            return False
        sum -= root.val     #对sum是否等于0的判定相当于原sum是否等于路径上的root.val之和
        if not root.left and not root.right:    #若是叶子节点，则直接确认是整条路径，进行判定即可
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)      #若不是叶子节点，则左右分别递归判定
# @lc code=end

