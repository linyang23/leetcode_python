#
# @lc app=leetcode.cn id=665 lang=python
#
# [665] 非递减数列
#

# @lc code=start
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 0
        for i in range(1, len(nums)):
            #只要当前值比下一个大，则res加一，当res大于1之后就无法修改一个成为递减数组了
            if nums[i - 1] > nums[i]:
                res += 1
                #防止越界
                if i < len(nums) - 1 and i > 1:
                    #若nums[i - 2] > nums[i]则无法用减小nums[i - 1]的方法来实现目标
                    #若nums[i + 1] < nums[i - 1]则无法用增大nums[i]的方法来实现目标
                    if nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]:
                        return False
            if res > 1:
                return False
        return True


# @lc code=end
