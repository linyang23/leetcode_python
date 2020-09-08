#
# @lc app=leetcode.cn id=447 lang=python
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        '''
        #直接在循环外创建字典是不行的，因为可能出现有2组没有重合点的‘点对’却等距离的情况
        #创建字典，存储格式为key为距离，value为同样距离出现的次数
        dic = {}
        '''
        for i in points:
            #每次循环新创建一个字典，用于存储与i点的距离, 存储格式为key为距离，value为同样距离出现的次数
            dic = {}    
            for j in points:
                if j != i:
                    #dic.get(key, default = None)，即若该key值不存在返回default指定的值
                    dic[(i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2] = dic.get((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2, 0) + 1
            for k in dic.values():
                if k > 0:
                    #排列问题，距离相同的n个点，在i点左右排列的可能数为An2，即n * (n - 1)
                    res += k * (k - 1)
        return res        
# @lc code=end

