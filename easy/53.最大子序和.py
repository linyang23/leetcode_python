#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        #res = nums[0]       #先默认以第一个数结尾的连续子数组和最大
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])    #此处的nums数组在i-1位置存储的是以第i-1个数结尾的最大连续子数组和，所以在i位置做对比的是第i个数 和 第i个数+以第i-1个数结尾的最大连续子数组和
            #res = max(res, nums[i])     #找出nums数组中最大的数
        return max(nums)
# @lc code=end

