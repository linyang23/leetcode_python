#
# @lc app=leetcode.cn id=453 lang=python
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #n - 1个数 + 1相当于 第n 个数 - 1
        #所以总次数就是把所有数变成最小的数需要的次数
        m = min(nums)
#总和减去m * len(nums)，即为把所有数变成最小的数需要的次数
        return sum(nums) - m * len(nums)       
# @lc code=end

