#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #collections.Counter函数的作用是统计str字符串中各字母的出现次数
        return collections.Counter(s) == collections.Counter(t)

# @lc code=end

