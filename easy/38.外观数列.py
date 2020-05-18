#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def next_num(tmp):      #定义推出下一个的函数
            res = ""
            i = 0
            tmp_n = len(tmp)
            while i < tmp_n:
                count = 1       #除了n=1的情况，实际上每2位数是1组，由count位 和 1或2 组成，且组数为总长度处以2
                while i < tmp_n - 1 and tmp[i] == tmp[i + 1]:       #查询是否出现连续相同的数，每出现一次count+1
                    count += 1
                    i += 1      #i是移动点
                res += (str(count) + tmp[i])
                i += 1
            return res
        res = "1"       #定义n=1的情况，方便从前往后推
        for i in range(1, n):
            res = next_num(res)
        return res
# @lc code=end

