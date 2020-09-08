#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        stack = []
        for i in nums2:
            #字典中存储的数据格式key为当前元素，value为下一个比其大的数
            while stack and i > stack[-1]:
                dic[stack.pop()] = i
            #stack为递减栈，只要比i小的部分，都会被放进字典
            stack.append(i)
        #在字典中查找i，若不存在，返回列表增加-1
        return [dic.get(i, -1) for i in nums1]
# @lc code=end

