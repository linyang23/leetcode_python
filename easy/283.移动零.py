#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #若nums为空数组，则返回空数组
        if not nums:
            return []
        #构建双指针
        j = 0
        #使用while然后i++会超时
        for i in xrange(len(nums)):
            #i用来遍历数组，每发现一个非零元素，则付给j指针所指的位置
            if nums[i]:
                nums[j] = nums[i]
                j += 1
            #非零元素找完后，后续其他位置全部置零
        for i in xrange(j, len(nums)):
            nums[i] = 0
        return nums
# @lc code=end

