#
# @lc app=leetcode.cn id=435 lang=python
#
# [435] 无重叠区间
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 贪心算法，按照区间尾部排序，然后找到能构成不重叠区间的区间最大数量，用
        # 总数量减去该数量即为要求的结果
        l1 = sorted(intervals, key = lambda x:x[1])
        res = 0
        num = float('-inf')
        for i in l1:
            #只要下一个区间的左值大于或者等于上一个被确定需要的区间的右值，则说明不重叠
            if i[0] >= num:
                res += 1
                num = i[1]
        return len(intervals) - res        
# @lc code=end

