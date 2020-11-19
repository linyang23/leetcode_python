#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 动态规划，状态转移方程为：
        # 当i>0且j=0时，dp[i][0] = dp[i-1][0] + grid[i][0]
        # 当i=0且j>0时，dp[0][j] = dp[0][j-1] + grid[0][j]
        # 当i>0且j>0时，dp[i][0] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])  # 得到行数m和列数n
        dp = [[0] * n for _ in range(m)]  # 得到m*n的全0矩阵
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
# @lc code=end
