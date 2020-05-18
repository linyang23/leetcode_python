#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[: : -1]:      #判定若s本身就是回文串，则输出s全部
            return s            
        max_len = 1             #先默认最大长度为1，最大回文部分为第一个字母
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1 , len(s)):
                if j - i + 1 > max_len and s[i : j + 1] == s[i : j + 1][: : -1]:        #判定，若发现回文且长度比之前更大，则更新回文长度max_len和回文字符串s[i : j + 1]
                    max_len = j -i + 1
                    res = s[i : j + 1]
        return res
# @lc code=end

