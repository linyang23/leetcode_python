#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #使用牛顿迭代法快速逼近平方根
        if num < 2:
            return True
        x = num // 2
        #使用此算法会得到不大于num的最大平方数的平方根，比如101->10，99->9
        while x ** 2 > num:
            x = (x + num // x) // 2
        return x ** 2 == num

# @lc code=end

