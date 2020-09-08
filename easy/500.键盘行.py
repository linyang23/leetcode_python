#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        w_1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
               'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        w_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        w_3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm',
               'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        for i in words:
            # set为转化为集合，对于哪些对重复不敏感的情况比较适用
            if set(i) <= set(w_1) or set(i) <= set(w_2) or set(i) <= set(w_3):
                res.append(i)
        return res
# @lc code=end
