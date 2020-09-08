#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #找到在1到n却不在nums中的数，即为要找的数
        return list(set(range(1, len(nums) + 1)) - set(nums))      
# @lc code=end

