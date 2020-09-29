#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        #找出各字母出现的最大位置
        last = {c: i for i, c in enumerate(S)}
        #k用来记录区间起始位置，j用来记录区间终止位置
        j = k = 0
        res = []
        for i, c in enumerate(S):
            #找到区间的终止位置（前面所有字符都在该区间内，即区间内所有字符的最大位置都小于等于j）
            j = max(j, last[c])
            if i == j:
                res.append(i - k + 1)
                k = i + 1
        return res
# @lc code=end

