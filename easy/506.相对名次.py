#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#

# @lc code=start
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        #另外设置一个列表，用于存储从大到小排序的输入数组，对应分数的下标即为名次，实现
        #分数和名次的对应
        nums1 = sorted(nums, reverse = True)
        for i in nums:
            #遍历nums中的值，如果其是前三名，则res列表添加对应的奖牌，其他则添加对应的名次
            if nums1.index(i) == 0:
                res.append('Gold Medal')
            elif nums1.index(i) == 1:
                res.append('Silver Medal')
            elif nums1.index(i) == 2:
                res.append('Bronze Medal')  
            else:
                res.append(str(nums1.index(i) + 1))
        return res        
# @lc code=end

