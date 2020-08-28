# 38 行 粗心了
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        l3 = None
        l3_head = l3
        
        while l1 != None or l2 != None:
            # base case
            if l3_head == None:
                if l1.val > l2.val:
                    l3_head = ListNode(l2.val)
                    l2 = l2.next
                else:
                    l3_head = ListNode(l1.val)
                    l1 = l1.next
                l3 = l3_head
            elif l1 == None:
                l3.next = l2
                break
            elif l2 == None:
                l3.next = l1
                break
            else:
                if l1.val > l2.val:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next        # l1 写成了 l2
                l3 = l3.next
        return l3_head
