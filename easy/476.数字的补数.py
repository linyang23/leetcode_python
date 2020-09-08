#
# @lc app=leetcode.cn id=476 lang=python
#
# [476] 数字的补数
#

# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #计算num的二进制长度（-2是因为转成字符串之后前面有前缀0b）
        tic = len(str(bin(num))) - 2
        tok = 2 ** tic - 1
        #将num与相同二进制长度的1111.11序列做异或，则为补数
        return num ^ tok

# @lc code=end

