#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #由于字符串不可修改，所以放在列表中处理
        ransom_l = list(ransomNote)
        magazine_1 = list(magazine)
        #从ransom中的第一个字符开始判断，若在magazine中，则删去该字符，并
        #判断下一个，以此类推，若出现一个不在，则返回false，若全部都在，则返回true
        for i in range(len(ransom_l)):
            if ransom_l[i] in magazine_1:
                magazine_1.remove(ransom_l[i])
            else:
                return False
        return True
# @lc code=end

