#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = str(digits)     #转成字符串，删除掉非数字的符号
        b = a.replace(',', ' ')
        b = b.replace('[', ' ')
        b = b.replace(']', ' ')
        b = b.replace(' ', '')
        c = int(b) + 1      #转为整型，进行加减运算
        d = [int(x) for x in str(c)]    #将整型转化为列表
        return d
        #d = str(c)          #转回字符串，方便转为列表
        #e = list(d)
# @lc code=end

