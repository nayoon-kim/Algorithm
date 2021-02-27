# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        prev = list1
        curr = list1.next
        
        while curr != None:
            if a-1 == count :
                while count != b:
                    curr = curr.next
                    count += 1
                prev.next = list2
                while list2.next != None:
                    list2 = list2.next
                list2.next = curr
            else:
                curr = curr.next
                prev = prev.next
                count += 1
        
        return list1