#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = 1e9
        minprice = int(inf)     #用于记录折线的起始点
        sum = 0     #用于记录所有需要的折线差
        diffprofit = 0      #用于运算折现差
        mp = -int(inf)      #mp用于记录上一个折现差
        for price in prices:
            diffprofit = max(price - minprice, diffprofit)      #找到局部最长的上升折线
            minprice = min(price, minprice)     #找到折线的起始点
            mp = diffprofit     #记录上一次运算中最长的折线
            if mp >= price - minprice:      #若上一次运算中最长的折线为局部最长，即上一条折线的末尾点为拐点（从上升转向平直或者下降）
                d = diffprofit      #记录局部的最大折现差，加入sum
                sum += d
                diffprofit = 0      #重置，寻找下一条局部最长上升的折线
                minprice = price    #重置折线起始点
                mp = -int(inf)      #重置折现差数据      
        return sum        
# @lc code=end

