#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #计算每个数值的平方和
        def next(n):
            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum
        seen  = set()
        #r如果n不等于1且不在哈希表里面，则继续计算
        while n != 1 and n not in seen:
            seen.add(n)
            n = next(n)
        #如果n == 1了，则返回True，如果n在哈希表里面了，则返回False
        return n == 1
# @lc code=end

