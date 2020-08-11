#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            #记录下一个节点
            tmp = cur.next
            #将当前节点指向pre,实际情况相当于把节点指向后面的方向改为指向之前，由于不再
            #指向后方，所以tmp是用来备份后方的地址的，防止找不到下一个节点
            cur.next = pre
            #pre和cur都前进一步
            pre = cur
            cur = tmp
        return pre
# @lc code=end

