#
# @lc app=leetcode.cn id=633 lang=python
#
# [633] 平方数之和
#

# @lc code=start
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # 双指针，通过剪枝减少时间复杂度
        b = int(sqrt(c)) + 1
        a = 0
        #大了就减少b，小了就增加a，如果a超过b之前都没有等于c，说明不存在这种组合
        while(a <= b):
            if a ** 2 + b ** 2 == c:
                return True
            elif a ** 2 + b ** 2 > c:
                b -= 1
            else:
                a += 1
        return False
# @lc code=end
