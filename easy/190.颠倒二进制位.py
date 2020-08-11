#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    #定义从2进制数中取出某一位值的函数       
    def reverseBits(self, n):
        def get_bit_val(byte, index):
            #一个二进制数与2的index次方做位与操作，即是将index处的值读出
            if byte & (1 << index):
                return 1
            else:
                return 0
        i = 0
        #根据2进制与10进制的关系，加和出10进制," <<x " 就相当于乘以2的x次方
        for j in range(32):
            i += get_bit_val(n, j) << (31 - j)
        return i       
# @lc code=end

