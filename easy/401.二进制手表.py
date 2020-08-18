#
# @lc app=leetcode.cn id=401 lang=python
#
# [401] 二进制手表
#

# @lc code=start
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """        
        # which用于将排列问题相对于组合问题的重复情况去除
        def backtrace(num, hour, minute, which):
            if hour > 11 or minute > 59:
                # 对于python，如果函数没有指定返回值，默认情况下会返回None
                return
            if num == 0:
                ''' f是求值，比如
                 name = 'Eric
                 'f'Hello, my name is {name}'
                 会转化为
                 'Hello, my name is Eric'
                :02是以2位数输出，比如1->01'''
                '''res.append(f'{hour}:{minute:02}')会报语法错误，原因未知'''
                txt = "{}:{:02}".format(hour, minute)
                res.append(txt)                
                return
            for h in range(which, 4):
                # 枚举hour的可能情况
                if h not in hour_seen:
                    hour_seen.add(h)
                    backtrace(num - 1, hour + int(pow(2, h)), minute, h + 1)
                    hour_seen.remove(h)
                # 枚举minute的可能情况
            for m in range(max(which, 4), 10):
                if m not in minute_seen:
                    minute_seen.add(m)
                    backtrace(num - 1, hour, minute + int(pow(2, m - 4)), m + 1)
                    minute_seen.remove(m)
        res = []
        hour_seen = set()
        minute_seen = set()
        backtrace(num, 0, 0, 0)
        return res


# @lc code=end
