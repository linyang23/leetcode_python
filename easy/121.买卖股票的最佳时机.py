#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = 1e9
        minprice = inf
        maxprofit = 0 
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)        #需要什么指标，就先构造出，再找可以的用方式，这里先将price - minprice构造出
            minprice = min(price, minprice)         #然后设置好price - minprice怎样从已知的地方来或者自行设置，后续可能需要迭代更新
        return maxprofit
# @lc code=end

