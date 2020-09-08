#
# @lc app=leetcode.cn id=485 lang=python
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        #创建res用于返回最大值，创建j用于遇1加1，遇0归0
        res = j = 0
        for i in range(len(nums)):
            if nums[i]:
                j += 1
                res = max(res, j)
            else:
                j = 0
        return res        
# @lc code=end

