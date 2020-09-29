#
# @lc app=leetcode.cn id=406 lang=python
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #由于相对于高个子，矮个子随便放在他们之间或者什么位置都不会影响其k值，所以我们
        #可以先操作高个子，再操作矮个子
        people.sort(key = lambda x:(-x[0], x[1]))
        res = []
        for i in people:
            #这里的插入操作完成后前面会有k个比自己高的
            res.insert(i[1], i)
        return res        
# @lc code=end

