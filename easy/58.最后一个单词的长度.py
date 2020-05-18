#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.split(' ')        #将字符串用已有的空格分割开
        for i in range(1, len(b) + 1):
            if b[len(b) - i] != '':
                return len(b[len(b) - i])
        return 0
# @lc code=end

