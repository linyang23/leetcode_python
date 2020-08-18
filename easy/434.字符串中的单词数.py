#
# @lc app=leetcode.cn id=434 lang=python
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #初始化count用于计数
        count = 0
        if not s:
            return 0
        #末尾加空格，使得即使末尾是非空格字符也会有非空格字符到空格的跳变
        s = s + ' '
        #计算非空格字符到空格的跳变数
        for i in range(len(s) - 1):
            if s[i] != ' ' and s[i + 1] == ' ':
                count += 1
        return count
# @lc code=end

