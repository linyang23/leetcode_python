#
# @lc app=leetcode.cn id=303 lang=python
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0]
        for i in range(len(nums)):
            #arr的第i + 1个数存储的为nums前i个数的和
            self.arr.append(self.arr[i] + nums[i])
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #nums的第i到j的数之和为arr的第j+1个数减去第i个数
        return self.arr[j + 1] - self.arr[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

