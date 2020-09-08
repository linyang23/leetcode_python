#
# @lc app=leetcode.cn id=504 lang=python
#
# [504] 七进制数
#

# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #不停的除7，余数的逆序排列即为7进制表示
        list1 = []
        res = ''
        #对于负数来说，只需要绝对值按照正数操作，然后前面加负号
        if num == 0:
            return '0'
        num1 = abs(num)
        while num1:
            list1.append(num1 % 7)
            num1 = num1 // 7
        #list中如果有数字不能直接使用join
        res = ''.join('%s' %id for id in list1)
        #做一个逆序输出
        if num > 0:
            return res[::-1]
        else:
            return '-' + res[::-1]
# @lc code=end

