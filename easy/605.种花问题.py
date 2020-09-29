#
# @lc app=leetcode.cn id=605 lang=python
#
# [605] 种花问题
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = 0
        fl = len(flowerbed)
        #找能插入的地方，能插入就插入，统计插入的数量，能达到n就说明至少能种下n朵花
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and fl > 1:
                if i != 0 and i != fl - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        #插入1后记得原地修改数组
                        flowerbed[i] = 1
                        res += 1
                elif i == 0:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        res += 1
                else:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        res += 1
            elif flowerbed[i] == 0 and fl == 1:
                if n <= 1:
                    return True
            elif n == 0:
                return True
        if res >= n:
            return True
        return False        
# @lc code=end

