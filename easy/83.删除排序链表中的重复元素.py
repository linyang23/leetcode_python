#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not (head and head.next):        #双指针法
            return head
        i, j = head, head
        while j:        #循环的功能为用j找到第一个与之前不同的数，然后用i表明替换的位置
            if i.val != j.val:
                i = i.next
                i.val = j.val
            j = j.next
        i.next = None
        return head
# @lc code=end

