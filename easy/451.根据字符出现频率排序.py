#
# @lc app=leetcode.cn id=451 lang=python
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        #使用collection得到频次字典
        dic = collections.Counter(s)
        #对字典按照频次升序排列
        dic2 = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        #根据排序后的字典将对应频次的字符依次添加到字符串中
        for key, value in dic2:
            res += key*value
        return(res[::-1])     
# @lc code=end

