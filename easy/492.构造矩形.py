#
# @lc app=leetcode.cn id=492 lang=python
#
# [492] 构造矩形
#

# @lc code=start
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #遍历找到符合要求的第一对长宽，因为从中间往外遍历，所以差距已经是最小的了
        for i in range(int(area ** 0.5), 0, -1):
            if not area % i:
                return [area / i, i]    
# @lc code=end

