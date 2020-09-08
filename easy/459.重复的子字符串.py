#
# @lc app=leetcode.cn id=459 lang=python
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """   
        #若移位i格，与原字符串重合，则说明可以由字符串重复多次构成,由于至少由
        #两个重复单元构成，所以最多检测右移一半就可以结束循环了
        for i in range(1, len(s) // 2 + 1):
            str1 = s[-i:] + s[:-i]
            if str1 == s:
                return True
        return False
# @lc code=end

