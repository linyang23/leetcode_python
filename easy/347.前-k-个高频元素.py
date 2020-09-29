#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        # 通过collections得到频率字典
        dic = collections.Counter(nums)
        #得到排名前k的的频率列表，通过列表中的频率输出对应的键
        value1 = sorted(list(dic.values()))[len(dic) - k: len(dic)]
        for key, value in dic.items():
            if value in value1:
                res.append(key)
        return res
# @lc code=end
