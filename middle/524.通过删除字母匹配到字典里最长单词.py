#
# @lc app=leetcode.cn id=524 lang=python
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        #对字符串列表降序排序
        d.sort(key=lambda x: (-len(x), x))
        def f(c):
            i = 0
            #遍历字符串中的字母
            for j in c:
                # 字符串中查找，i参数为查找起点
                k = s.find(j, i)
                if k == -1:
                    return False
                #如果找到该字母，则i = k + 1，做到一一对应的查询
                i = k + 1
            #如果所有的字母都能在s中一一对应且按照顺序的找到，则说明可以通过删除s的字母得到c
            return True
        #遍历d中的字符串
        for c in d:
            if f(c):
                return c
        #若没有则返回空字符串
        return ''
# @lc code=end
