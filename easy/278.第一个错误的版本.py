#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分查找，l为返回的最初错误版本
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            #若m处有问题，则在l到m中继续二分查找
            if isBadVersion(m):
                r = m
            #若m处无问题，则在m+1到r中继续二分查找
            else:
                l = m + 1
        return l
# @lc code=end

