#
# @lc app=leetcode.cn id=521 lang=python
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        #额，如果有个字符串比对面长，其本身就不能是其他字符串的子序列
        if a == b:
            return -1
        return max(len(a), len(b))
# @lc code=end

