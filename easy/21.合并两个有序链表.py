#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:         #val 是当前节点的值 next 是指向下一个节点的指针/引用
                l1, l2 = l2, l1         #因为l1,l2都是有序链表，所以新链表的下一个节点一定是从两个链表未排序的各自第一个节点中选择比较小的
            l1.next = self.mergeTwoLists(l1.next, l2)       #递归，不断找到两个链表未排序的最小值进行连接
        return l1 or l2         #若l1为空，返回l2
# @lc code=end

