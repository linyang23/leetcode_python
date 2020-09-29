#
# @lc app=leetcode.cn id=452 lang=python
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #同样是求不重叠区间问题，贪心算法解决
        a = sorted(points, key = lambda x:x[1])
        res = 0
        nums = float('-inf')
        for i in a:
            #注意这里不能取等号，因为对于气球问题哪怕是端点重叠也算作重叠
            if i[0] > nums:
                res += 1
                nums = i[1]
        return res      
# @lc code=end

