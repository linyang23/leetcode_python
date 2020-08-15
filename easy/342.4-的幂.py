#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        # 求log4（num）,若为整数则是4的幂次
        a = log10(num) / log10(4)
        # floor(x)为取不大于x的最大整数
        return a == floor(a)
        
# @lc code=end

