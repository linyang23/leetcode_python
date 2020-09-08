#
# @lc app=leetcode.cn id=475 lang=python
#
# [475] 供暖器
#

# @lc code=start
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = []
        #双指针法，各指针指向左右的供暖器
        pin1 = 0
        pin2 = 1
        houses = sorted(houses)
        #当只有一个供暖器时,最远距离要么出现在房屋最左侧，要么出现在最右侧
        if len(heaters) == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[len(houses) - 1] - heaters[0]))
        #当有多个供暖器时
        heaters = sorted(heaters)
        #遍历房间
        for house in houses:
            #找到被指定房屋前后最近的供暖器（特殊情况为房屋太靠后，
            #所以只能得到左边的两个最近供暖器）
            while pin2 < len(heaters) - 1 and heaters[pin2] < house:
                pin1 += 1
                pin2 += 1
            #计算最近供暖器的距离
            res. append(min(abs(heaters[pin1] - house), abs(heaters[pin2] - house)))
        #找到res中的最大值，即为最小加热半径
        return max(res)
# @lc code=end

