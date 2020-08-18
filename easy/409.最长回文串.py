#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #贪心算法
        ans = 0
        #collections.Counter的功能是统计字符出现的字数并放在counter字典中
        count = collections.Counter(s)
        #由于题目要求是找到通过这些字母能构造出的最长回文串长度，而回文串规律为(x)y(x)
        #所以只要是偶数次的字符都能加入，使长度+（偶数次），而奇数次的只能有一个做中心，
        #使长度+（奇数次），其他奇数次都只能使长度加（奇数次 - 1）
        for v in count.values():
            #若奇数次的字符有n种，则需要减去n - 1
            if ans % 2 == 1 and v % 2 == 1:
                ans -= 1
            ans += v
        return ans
# @lc code=end

