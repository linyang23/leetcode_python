#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:        #若数组为空，则left = 0，right = -1
                return None
            p = (left + right) // 2        #找到数组中间点，数组左侧的放左边节点，数组右侧的放右边节点
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)       #中序遍历，始终找到二分的中间，不断二分排列节点
            return root
        return helper(0, len(nums) - 1)
# @lc code=end

