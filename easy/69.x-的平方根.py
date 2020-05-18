#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:           #牛顿迭代法，不断逼近的方式
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        cur = 10        #cur可任意设置
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:   #精度设置，说明已经非常逼近了
                return int(cur)
# @lc code=end

