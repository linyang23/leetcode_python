#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        global res
        res = 0
        #反序中序遍历
        def mid(root):
            global res
            #标准模式，先设置根节点然后设置对右节点递归，然后处理，然后设置对左节点递归
            if not root:
                return
            mid(root.right)
            res += root.val
            root.val = res
            mid(root.left)
            return
        mid(root)
        return root            
# @lc code=end

