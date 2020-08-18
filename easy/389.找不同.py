#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #用列表处理字符串
        s_l = list(s)
        t_l = list(t)
        #若找到都有的，则在s中删去，最终找到t中有而s中没有的
        for i in range(len(t_l)):
            if t_l[i] in s_l:
                s_l.remove(t_l[i])
            else:
                return t_l[i]        
# @lc code=end

