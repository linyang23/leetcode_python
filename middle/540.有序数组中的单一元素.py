#
# @lc app=leetcode.cn id=540 lang=python
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #二分查找
        lo = 0
        hi = len(nums) - 1        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid - 1] == nums[mid]:
                if (mid - 1 - lo) % 2:
                    hi = mid - 2
                else:
                    lo = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (hi - mid - 1) % 2:
                    lo = mid + 2
                else:
                    hi = mid - 1
            else:
                return nums[mid]
        return nums[lo]
# @lc code=end

