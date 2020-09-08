#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #将按位异或的结果转成二进制并继续转成字符串
        res = str(bin(x ^ y))
        #查询字符串中1的个数，即为汉明距离
        dic = collections.Counter(res)
        return dic['1']        
# @lc code=end

