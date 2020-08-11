#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        dic = {}
        for in in range(len(s)):
            if s[i] not in dic:
# @lc code=end

