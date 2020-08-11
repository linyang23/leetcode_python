#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #创建哨兵节点，使得所有删除点的情况都不是链表头部
        sentinel = ListNode(0)
        sentinel.next = head
        #curr为当前节点，prev为前继节点
        prev, curr = sentinel, head
        while curr:
            #若相等，则删除该节点，方法为将前继节点的后续替换为该节点的后续
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next
# @lc code=end

