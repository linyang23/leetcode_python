#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #每整除一次26,就加上一个字母，直到比26小
        return '' if not n else self.convertToTitle(n // 26 - (0 if n % 26 else 1)) + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n % 26 - 1 if n % 26 else 26 - 1]
# @lc code=end

