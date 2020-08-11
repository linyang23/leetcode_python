#
# @lc app=leetcode.cn id=172 lang=python
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #观察一个阶乘中的规律可以发现，质因数为5的个人大于质因数为2的个数
        i = 0
        #5个个数就是0的个数，而5的个数等于n/5 + n/25 + n/125...（看n属于哪个区间而定）
        while n:
            i += n // 5
            n = n // 5
        return i
# @lc code=end

