#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #动态规划，状态转移方程为:
        # 当i>0且j=0时，dp[i][0] = dp[i - 1][0]
        # 当i>0且j=0时，dp[0][j] = dp[0][j - 1]
        # 当i>0且j>0时, dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]

# @lc code=end

