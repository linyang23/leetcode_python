#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #若没有房屋，则无房可偷
        if not nums:
            return 0
        #若只有一间房屋，则偷这一家
        if len(nums) == 1:
            return nums[0]
        #若有两间房屋，则偷取最大值    
        #若有k（k>2）间房屋，则有两种方案，一种是偷取第k间，然后加上前k-2间的最大值，或者不偷取第k间，直接获取前k-1间的最大值，最终方案是这两种方案的最大值
        #递归会超时
        '''
        return max(self.rob(nums[: -1]), self.rob(nums[: -2]) + nums[len(nums) - 1])
        '''
        #second用于记录需要的最大值，first用于记录k-2的最大值
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)
        return second
# @lc code=end

