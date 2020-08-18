#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list_a = []
        #在nums2中寻找nums1的元素，若nums2有该元素，则将nums1中的该元素添加到新的列表
        # ，并将nums2中该元素删除，以防止重复添加
        i = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                list_a.append(nums1[i])
                nums2.remove(nums1[i])        
        return list_a
        
# @lc code=end

