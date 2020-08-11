#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicts = set()
        for i in nums:
            if i in dicts:
                return True
            dicts.add(i)
        return False
# @lc code=end

