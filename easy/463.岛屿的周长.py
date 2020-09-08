#
# @lc app=leetcode.cn id=463 lang=python
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        #遍历所有格子
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #遇见为1的格子，加4条边
                if grid[i][j]:
                    res += 4
                    #如果为1的格子左边或上面有其他为1的格子，需要减去相应的边
                    if i and grid[i - 1][j]:
                        res -= 2
                    if j and grid[i][j - 1]:
                        res -= 2
        return res        
# @lc code=end

