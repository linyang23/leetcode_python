#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #不使用排序，我们用二分法查找，判定条件：左侧数字比自己大
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            #其实很好理解，变化点及其右侧元素会都小于其左侧元素
            #若中间元素比右侧元素小，则说明变化点在中间元素右侧
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
# @lc code=end

