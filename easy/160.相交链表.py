#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #???????
        curl1 = headA
        curl2 = headB
        #????????????NULL??????,?????????NULL
        while curl1 != curl2:
            curl1 = curl1.next if curl1 else headB
            curl2 = curl2.next if curl2 else headA
        return curl1
        
# @lc code=end

