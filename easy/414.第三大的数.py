#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        #若字典不到3个key值，说明没有第3大的数，直接返回最大值
        if len(count) < 3:
            return max(nums)
        #对字典按照key进行排序，返回倒数第3个
        return sorted(count)[-3]        
# @lc code=end

