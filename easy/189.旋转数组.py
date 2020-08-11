#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #??k?????????????????????
        n = len(nums)
        k = k % n
        #??????
        def swap(l, r):           
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)
# @lc code=end

