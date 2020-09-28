#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution(object):
    # 写函数用于判断是否为回文串
    def isPalindrome(self, s, i, j):
        while(i < j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 当遇到不匹配的时候，判断删除左边或删除右边是否有一种剩下的是回文串
        i, j = 0, len(s) - 1
        while(i < j):
            if s[i] != s[j]:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j - 1)
            else:
                i += 1
                j -= 1
        return True
# @lc code=end
