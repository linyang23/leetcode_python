#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #做一个标准转换，如果转换前后没有差别，则说明本身就是标准模式
        if word == word.capitalize() or word == word.upper() or word == word.lower():
            return True
        return False
# @lc code=end

