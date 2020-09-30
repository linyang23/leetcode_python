#
# @lc app=leetcode.cn id=744 lang=python
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        #二分查找缩小区间，然后在区间内从小到大遍历
        l = len(letters)
        while letters[int(l / 2)] > target and l != 0:
            l = int(l / 2)
        #使用min防止溢出
        for i in range(int(l / 2), min(l + 1, len(letters))):
            if letters[i] > target:
                return letters[i]
        return letters[0]
# @lc code=end

