#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = 0       #0和任何数异或的结果为这个数本身
        for num in nums:
            d ^= num    #两个相同的数异或结果为0
        return d
# @lc code=end

