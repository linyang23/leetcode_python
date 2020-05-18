#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        d = len(nums)
        haystack = str(nums)        #转化为字符串，用28题思路求解
        b = haystack.split('[')[1]
        c = b.split(']')[0]
        n = len(haystack)
        for i in range(0, d):
            if int(c.split(',')[i]) >= target:
                return i
        return d
# @lc code=end

