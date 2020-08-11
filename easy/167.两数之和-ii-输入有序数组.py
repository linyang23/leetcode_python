#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #双指针法
        i, j = 0, len(numbers) - 1
        #如果i >= j了就可以终止了，因为不符合题目要求，且后续工作重复
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            #若小了那么肯定是i不够大，因为j已经是最大了
            elif numbers[i] + numbers[j] < target:
            #若大了那么肯定是j不够小，因为i已经是最小了
                i += 1
            else:
                j -= 1
# @lc code=end

