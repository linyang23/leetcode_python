#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #将较短的设为1，较长的设为2
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        res = ''
        k = len(num1) - 1
        carry = 0
        #从len(num2) - 1逆序循环，因为是从字符串末尾开始相加
        for i in range(len(num2) - 1, -1, -1):
            if k >= 0:
                #利用k和i的同步减1，实现从字符串末尾开始同步相加
                add = int(num2[i]) + int(num1[k]) + carry
                k -= 1
            #当k<0的时候，说明num1已经被加完了
            else:
                add = int(num2[i]) + carry
            #carry为进位，只要add超过了10，就需要进位了
            carry = add // 10
                #进位之后，add去掉进位需要的部分
            res += str(add % 10)
        #由于后面的数字先加出来先输出，所以需要逆序运算一次
        res = res[:: -1]
        #计算完之后还有个进位数不知道是1还是0，所以还需要看是否需要进位输出
        return '1' + res if carry > 0 else res
# @lc code=end

