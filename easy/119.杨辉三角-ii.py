#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)      #创建足够存储的列表
        res[0] = 1
        for i in range(rowIndex + 1):
            res[i] = 1
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res
# @lc code=end

