#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #在nums2中寻找nums1的元素，若nums2没有该元素，则将nums1中的该元素删除
        #for i in range(len(nums1)):
        #不能用for是因为i会在后续过程中变化，容易出错
        i = 0
        while i < len(nums1):
            if nums1[i] not in nums2:
                nums1.pop(i)
                i -= 1
            i += 1
        #由于重复元素只保留一个，所以需要去重
        return list(set(nums1))
        
# @lc code=end

