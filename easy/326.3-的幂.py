#
# @lc app=leetcode.cn id=326 lang=python
#
# [326] 3的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        #求log3（n）,若为整数则是3的幂次
        a = log10(n) / log10(3)
        #floor(x)为取不大于x的最大整数
        return a == floor(a)
        
# @lc code=end

