#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #使用两个栈来模拟队列，这里初始化两个栈
        self.s1 = []
        self.s2 = []
        #初始化一个变量，用于读出队列peek值
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        #新元素总是从s1压入
        if not self.s1:
            #由于front未设置初值，所以这里设置一次
            self.front = x
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                #由于队列和栈出入特性不同，这里将s1的元素依次弹出到s2，实现与队列特性对应
                self.s2.append(self.s1.pop())
            self.front = None
        return self.s2.pop()



    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        #若s2为空，则说明元素在s1存储，这时使用front，若s2不为空，则说明元素在s2存储，这
        #时使用s2的弹出功能
        if self.s2:
            return self.s2[-1]
        return self.front


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        #若s1和s2均为空，则说明队列无元素，输出false，否则输出true
        if not self.s1 and not self.s2:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

