#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #???2???2????????1????????1??
        while n > 1:
            n = float(n)
            n /= 2
        return n == 1
# @lc code=end

