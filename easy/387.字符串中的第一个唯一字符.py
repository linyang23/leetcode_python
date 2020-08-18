#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_l = list(s)
        n = {}
        n_l = []
        solution = []
        #对重复字符value置2，非重复字符value置1
        for i in range(len(s_l)):
            if n.get(s_l[i]):
                n[s_l[i]] = 2
            else:
                n[s_l[i]] = 1
        '''        
        #字典反转，方便查询value对应的key,但是这样遇见value为1的key有多个的情况会失效
        new_dict = {v : k for k, v in s_l.items()}
        return new_dict[1]
        '''
        #定义根据value查找key的函数
        def get_keys(d, value):
            return [k for k, v in d.items() if v == value]
        #返回value为1的第一个key
        n_l = get_keys(n, 1)
        #若列表为空，说明不存在非重复字符
        if not n_l:
            return -1
        #由于列表中只是不重复的【字符】，所以还需要求出【索引】
        for j in range(len(s_l)):
            if s_l[j] in n_l:
                solution.append(j)
        #返回最小索引
        return min(solution)
# @lc code=end

