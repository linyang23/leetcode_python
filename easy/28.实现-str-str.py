#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':        #判定为空，返回0
            return 0
        L, n = len(needle), len(haystack)
        for i in range(n - L + 1):      #先判定needle首字母是否出现
            if haystack[i] != needle[0]:
                continue
            if haystack[i : i + L] == needle:       #首字母出现后判定是否为needle
                return i
        return -1  
# @lc code=end

