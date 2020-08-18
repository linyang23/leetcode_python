#
# @lc app=leetcode.cn id=371 lang=python
#
# [371] 两整数之和
#

# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #偷懒算法
        list_a = []
        list_a.append(a)
        list_a.append(b)
        return sum(list_a)
        '''
        
        #使用异或代替无进位加法，与运算左移代替进位，合起来的总运算为有进位加法
        while(b != 0):
            temp = a ^ b
            b = (a & b) << 1
            a = temp
        return a     
        '''       
        
# @lc code=end

