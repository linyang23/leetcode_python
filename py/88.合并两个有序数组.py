#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[: m]     #复制出新的数组用于比较，原数组用于存储比较后的结果,通过id函数可以发现只有通过nums1[: m]才会给nums1_copy分配新id
        nums1[: ] = []
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:      #双指针法
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2: ] = nums1_copy[p1: ]
        if p2 < n:
            nums1[p1 + p2: ] = nums2[p2: ]
# @lc code=end

