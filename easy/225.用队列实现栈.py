#
# @lc app=leetcode.cn id=225 lang=python
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #初始化，生成一个双向队列对象q
        self.q = collections.deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        for i in range(len(self.q) - 1):
            #列表元素依次从左侧推出，然后重新从右侧append进入，目的在于
            # 将append的元素放在最左侧,因为对栈来说入栈从左边进入，而队
            # 列是从右边读入的
            self.q.append(self.q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        #列表的左侧推出
        return self.q.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        #取到列表的头部
        return self.q[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        #判断列表是否为空
        return not len(self.q)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

