#
# @lc app=leetcode.cn id=413 lang=python
#
# [413] 等差数列划分
#

# @lc code=start
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 动态规划：
        # 若前面不构成等差数列，那么添加数字构成等差数列会使可能数+1
        # 若前面构成等差数列，那么添加数字构成等差数列会使可能数的增加数为等差数列的位数-1
        # 比如123 + 4，可能数增加2
        # 而1234 + 5，可能数增加3
        # 而12345 + 6，可能数增加4
        dp = [0] * len(A)
        for i in range(2, len(A)):
            # 判断添加数字后是否构成等差数列
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)
# @lc code=end
