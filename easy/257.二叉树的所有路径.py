#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                #若root为叶子节点，则该条路径遍历结束
                if not root.left and not root.right:
                    #注意path和paths不是一个量，path是字符串，paths是列表
                    paths.append(path)
                #若root不是叶子节点，则继续递归
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
        #定义列表，用于存储不同的路径
        paths = []
        construct_paths(root, '')
        return paths
# @lc code=end

