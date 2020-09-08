#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        x0 = 0
        x1 = 1
        x2 = 1
        #没什么好说的，递归就完事了
        if N == 0:
            return x0
        if N == 1:
            return x1 
        if N == 2:
            return x2
        for i in range(N - 2):
            x2, x1, x0 = x2 + x1, x2, x1
            print(x2, x1, x0)
        return x2        
# @lc code=end

