#
# @lc app=leetcode.cn id=443 lang=python
#
# [443] 压缩字符串
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #双指针法，一个读，一个写,anchor指向连续字符串的起始位置
        anchor = write = 0
        for read, c in enumerate(chars):
            # 找到连续字符串末尾（为防止最后一个字符时越界所以加上找到
            # 整个字符串末尾作为连续字符串末尾）
            if read + 1 == len(chars) or chars[read + 1] != c:
                #写入指针从连续字符串首部开始运作，这里写入字符
                chars[write] = chars[anchor]
                #每写入一次数据，write + 1
                write += 1
                #这里写入次数
                if read > anchor:
                    #这样写是为了让大于等于10次的次数可以占据多个数组格写入
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                #这里是字符只出现了一次就变成下一个字符或者终止了
                anchor = read + 1
        #写入了几次就说明数组的新长度是多少
        return write
# @lc code=end

