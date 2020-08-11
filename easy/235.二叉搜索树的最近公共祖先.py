#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #定义当前节点,p节点,q节点
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        #如果p、q都比母节点大,说明最近公共祖先是在母节点的右侧
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        #如果p、q都比母节点小，说明最近公共祖先是在母节点的左侧
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        #如果p、q一个比母节点大，一个比母节点小，说明母节点就是最近公共祖先
        else:
            return root        
# @lc code=end

