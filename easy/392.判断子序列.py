#
# @lc app=leetcode.cn id=392 lang=python
#
# [392] 判断子序列
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #双指针法
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        #判断最终相等的字符数是否等于s的长度
        return i == len(s)
# @lc code=end

