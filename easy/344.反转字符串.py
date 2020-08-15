#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
        #第一个和最后一个互换，第二个和倒数第二个互换，以此内推
        while i < n // 2:
            s[i], s[n - 1 - i] = s[n - 1 -i], s[i]
            i += 1
        return s
# @lc code=end

