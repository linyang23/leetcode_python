#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#

# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #从i等于1行开始找n所在的区间，不在就i+1继续找
        i = 1
        while n >= i * (i + 1) / 2:
            i += 1
        return i - 1                       
# @lc code=end

