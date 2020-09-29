#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #使用collections得到频次表
        res = []
        dic = collections.Counter(nums)
        #原地修改
        for i in range(len(nums)):
            if i < dic[0]:
                nums[i] = 0
            elif i < dic[0] + dic[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums
# @lc code=end

