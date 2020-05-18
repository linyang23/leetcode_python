#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0       #若为空，则返回0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]       #通过遍历，找到每一个和之前不同的数，然后i计数+1，并将此不同的数复制到该位置上
        return i + 1            #此处加1是因为要算上本身只要不为空，则至少有一个不同的数
# @lc code=end

