#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        #贪心算法，先满足胃口最小的孩子，以及用符合条件的最小饼干来满足胃口最小的孩子。
        s = sorted(s)
        g = sorted(g)
        #双指针，gi指向最小的孩子，si指向最小的饼干
        gi = si = 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                #每满足一个最小的孩子，则gi + 1,gi的值即为被满足的人数
                gi += 1
            si += 1
        return gi        
# @lc code=end

