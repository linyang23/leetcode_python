#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())]       #*用于对filter返回的迭代器解包
        return s == s[: : -1]       #对称判定
# @lc code=end

