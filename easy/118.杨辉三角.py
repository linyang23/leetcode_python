#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:        #构造递归元
            return []
        if numRows == 1:
            return [[1]]
        upper = self.generate(numRows - 1)
        upper.append([1] +[upper[-1][i - 1] + upper[-1][i] for i in range(1, numRows - 1)] + [1])
        return upper
# @lc code=end

