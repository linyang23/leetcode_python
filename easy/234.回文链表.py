#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #??????????????
        #if not head and not head.next???
        if not (head and head.next):
            return True
        #??????????????
        p = ListNode(-1)
        p.next, low, fast = head, p, p
        #?????????????????2n+1???n+(n+1),??2n?????n+n
        while fast and fast.next:
            low, fast = low.next, fast.next.next
        #????????cur?pre?????????????
        cur, pre = low.next, None
        #????????
        low.next = None
        #??????
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        #?????????
        a, b = p.next, pre
        #???????????????
        while b:
            if b.val != a.val:
                return False
            b, a = b.next, a.next
        return True
# @lc code=end

