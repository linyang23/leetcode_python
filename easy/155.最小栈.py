#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

#append输入的为（x,min(x,self.stack[-1][-1]）,故append中每个值右边的部分为最小值
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

#虽然pop时可能会将已经算好的最小值删去，但是由于每次入栈都会重新计算最小值，所以不影响
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

#[-1][0]为正常输入的x
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

#[-1][0]为辅助记录的最小值
    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

