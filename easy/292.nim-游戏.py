#
# @lc app=leetcode.cn id=292 lang=python
#
# [292] Nim 游戏
#

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #要赢就得把4留给对面而不能自己拿到,通过这个思想发现只要石头
        # 数量不是4的倍数就总能赢
        if not n % 4:
            return False
        return True        
# @lc code=end

