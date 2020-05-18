#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if (-2 ** 31 <= x <= 2 ** 31 - 1) & (x != 0):
            strx = str(x)       #将数字转化为字符串
            a = len(strx)       #获取长度，用于翻转
            z = ' '
            if x < 0:
                z = '-' + strx[-1 : -a : -1]        #若x负数，比如为-432,则z='-' + 234（strx[-1 : -a : -1]截取字符时只截取数字不截取'-'）
            else:
                z = strx[: : -1]                    #若x为整数，则直接翻转
            z1 = int(z)         #转化回int型，若z翻转后为023，则转化后只保留23，解决掉了原输入x末尾数字为0的情况
            if -2 ** 31 <= z1 <= 2 ** 31 - 1:
                return z1
            else:
                return 0        #超过数值范围则输出为0
        return 0
# @lc code=end

