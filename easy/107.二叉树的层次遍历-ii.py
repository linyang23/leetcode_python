#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        #层次遍历，即为同深度的点放在同一组，然后深度越大的放在前面的组
        if not root:
            return []
        res = {}        #创建字典用于记录
        def dfs(r, n):    #一步步从上往下递归穷举然后加入字典  
            if n in res:        #若字典中已经有该深度的组，直接将该值加入该深度对应的组
                res[n].append(r.val)
            else:           #若字典中无该深度的组，则添加该组
                res[n] = [r.val]
            if r.left:      #每经过一个节点，深度加1
                dfs(r.left, n + 1)
            if r.right:
                dfs(r.right, n + 1)
        dfs(root, 1)
        c = [res[k] for k in sorted(res.keys(), key = lambda x: x, reverse = True)]
        return c      #元组构成的列表排序用法
            

# @lc code=end

