#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        i , j = 0, 0
        #判断s是否为空，若为空，则说明已将所有字母计算完毕
        while len(s):
            #每进入一次循环，i的权重提高26倍
            j += (ord(s[-1]) - 64) * 26 ** i
            i += 1
            s = s[: -1]
        return j
        
# @lc code=end

