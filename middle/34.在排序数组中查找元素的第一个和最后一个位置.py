#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums) - 1        
        res = []
        #二分法，找到包含target的区间，若没有，返回[-1, -1]
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid
            else:
                break
        #对该区间进行查找
        for i in range(lo, hi + 1):
            if nums[i] == target:
                res.append(i)
        if not len(res):
            return [-1, -1]
        return [res[0], res[len(res) - 1]]      
# @lc code=end

