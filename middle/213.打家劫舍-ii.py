#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划问题，转移方程为 dp[n+1] = max(dp[n],dp[n-1]+num)
        def rob(nums):
            pre, cur = 0, 0  # 通过pre和cur降低空间复杂度
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        # 对于环形的房屋（数量大于等于2），有两种情况，一种是抢第一间不抢最后一间，一种是抢最后一间不抢第一间
        if not len(nums):
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(rob(nums[: -1]), rob(nums[1:]))

# @lc code=end
