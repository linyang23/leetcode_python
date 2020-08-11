#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        #定义从2进制数中取出某一位值的函数 
        def get_bit_val(byte, index):
            #一个二进制数与2的index次方做位与操作，即是将index处的值读出
            if byte & (1 << index):
                return 1
            else:
                return 0
        i = 0
        #逐位判断是否为1
        while n:
            if get_bit_val(n, 0):
                i += 1
            n = n >> 1
        return i        
# @lc code=end

