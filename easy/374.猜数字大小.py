#
# @lc app=leetcode.cn id=374 lang=python
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #先猜测n，若大了，则猜测所猜数的一半，若小了，则猜测所猜数与之前偏大所猜数的一半，由此迭代
        while guess(n) != 0:
            if guess(n) == -1:
                res = n             
                n = n // 2
            if guess(n) == 1:
                n = (n + res) // 2
        return n        
# @lc code=end

