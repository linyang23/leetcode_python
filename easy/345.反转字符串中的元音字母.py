#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #做查找表，只有在其中的才互换
        lookup = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        #由于python中字符串不可修改，于是转化成列表处理
        s_list = list(s)
        #定义左右指针，用于递进查找
        i = 0
        j = len(s_list) - 1
        #第一个元音和最后一个元音互换，第二个元音和倒数第二个元音互换，以此内推
        while i < j:            
            if s_list[j] not in lookup:
                j -= 1
            if s_list[i] not in lookup:
                i += 1
            if s_list[i] in lookup and s_list[j] in lookup:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
        #str.join(list)是将列表中各部分用str连接成字符串
        return ''.join(s_list)        
# @lc code=end

