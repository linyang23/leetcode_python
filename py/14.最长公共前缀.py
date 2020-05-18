#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return  ''
        s = strs[0]
        for i in range(1, len(strs)):       #由于是前缀，所以可以通过遍历删除末尾的方式；由于自身肯定与自身重合，所以range从1开始
            while strs[i].find(s) != 0:     #find() 方法检测字符串中是否包含子字符串,如果包含子字符串返回开始的索引值，否则返回-1
                s = s[: -1]
        return s
# @lc code=end

