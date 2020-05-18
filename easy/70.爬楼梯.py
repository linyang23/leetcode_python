#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #易知，上n级台阶可以先上n-2级然后上2级，或者先上n-1级然后上1级
        climb = {}
        climb[0] = 1
        climb[1] = 1
        climb[2] = 2
        for i in range(3,  n + 1):
            climb[i] = climb[i - 1] + climb[i - 2]
        return climb[n]
        '''def climbS(n):       #递归算法会超时
            if n <= 1:
             return 1
            return climbS(n - 1) + climbS(n - 2)
        return climbS(n)
        '''
# @lc code=end

