#
# @lc app=leetcode.cn id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solu = []
        #主要range中的值，不是range(n)，应该根据实际情况判定
        for i in range(1, n + 1):
            #分类讨论
            if i % 3 == 0:
                if i % 5 == 0:
                    solu.append('FizzBuzz')
                else:
                    solu.append('Fizz')
            elif i % 5 == 0:
                solu.append('Buzz')
            else:
                #将数字转为字母加入列表
                solu.append("{}".format(i))
        return solu       
# @lc code=end

