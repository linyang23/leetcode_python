#
# @lc app=leetcode.cn id=532 lang=python
#
# [532] 数组中的K-diff数对
#

# @lc code=start
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict = {}
        res = 0
        #若nums中的某个数+k(k != 0)仍在nums中，说明该数和该数+k构成一个k-diff对
        if k > 0:
            for i in nums:            
                if i + k in nums and i not in dict:
                    dict[i] = i + k
            return len(dict)
        #若k = 0，则统计出现次数达到2次的数字，其个数即为k-diff对数
        elif k == 0:
            dict = collections.Counter(nums)
            for k, v in dict.items():
                if v >= 2:
                    res += 1
            return res   
        #绝对值之差不能小于0
        else:
            return 0           
# @lc code=end

