#
# @lc app=leetcode.cn id=405 lang=python
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_str = '0123456789abcdef'
        #&运算都是转化为二进制再运算，此处为高位补0操作
        num &= 0xffffffff
        digits = []
        if num == 0:
            return '0'
        while num:
            #取二进制表示的最后四位以转化为十六进制
            lowbit4 = num & 0xf
            #删掉这最后四位
            num >>= 4
            #根据二进制找到十六进制的表示
            digits.append(hex_str[lowbit4])
            #由于后面的数放在列表的前面，所以需要reverse一下
        return ''.join(reversed(digits))
        
# @lc code=end

