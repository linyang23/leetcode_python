#
# @lc app=leetcode.cn id=501 lang=python
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # deque是一个双端队列
        queue = collections.deque()
        # 将整个树存入queue
        queue.append(root)
        res = []
        ans = []

        while queue:
            for _ in range(len(queue)):
                # popleft，queue去掉树的一层，赋给node
                node = queue.popleft()
                # 将去掉的那个点的值赋给ans
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # most_common用于统计出现的次数,返回的数字对列表，
        # 因为取key值不方便，所以迂回一下
        tmp = collections.Counter(ans).most_common()
        for k, v in tmp:
            if v == tmp[0][1]:
                res.append(k)
        return res

# @lc code=end
