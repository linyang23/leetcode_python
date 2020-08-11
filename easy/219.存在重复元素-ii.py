#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #用字典保存
        dic = {}
        #若
        for i in range(len(nums)):
            #若发现有相同的数且k >= i -dic[nums[i]](i是后面出现的重复数位置
            # ，dic[nums[i]])是前面出现的重复数位置
            if nums[i] in dic and dic[nums[i]] >= i - k:
                return True
            #若未发现，则加入索引
            dic[nums[i]] = i
        return False
# @lc code=end

