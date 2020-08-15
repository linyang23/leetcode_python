#
# @lc app=leetcode.cn id=263 lang=python
#
# [263] 丑数
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #??0??????
        if not num:
            return False
        #???2?3?5???????1?????
        while num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            if not num % 2:
                num /= 2
            if not num % 3:
                num /= 3
            if not num % 5:
                num /= 5
        return num == 1
# @lc code=end

