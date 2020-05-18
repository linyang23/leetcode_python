#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        #由于遍历时经过特殊规则双字符时，会将单独第一个字符和两个字符同时计入加和，所以d中特殊字符的值是真正值减去第一个字符的值，比如IV实际为4，但是表中为实际值4-I的值1=3，以此抵消计算规则所带来的偏差
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD':300, 'D': 500, 'CM': 800, 'M': 1000}
        return sum(d.get(s[max(i - 1, 0): i + 1], d[n]) for i, n in enumerate(s))       
        #max函数用于防止遍历第一个字符时出现[-1:0]的情况
        #enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标

# @lc code=end

