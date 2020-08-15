#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #通过手写对照数字的对应（1-1,2-2,...,9-9,10-1,11-2..），可以发现对应的一位数
        # 按9进行循环（除开0，其他能整除9的加和结果均为9）
        r = num % 9
        if not num:
            return 0
        if r:
            return r
        return 9
# @lc code=end

