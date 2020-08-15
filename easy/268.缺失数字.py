#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 缺失数字
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #???0?n???????????
        l = len(nums)
        res = l * (l + 1) / 2
        return res - sum(nums)
# @lc code=end

