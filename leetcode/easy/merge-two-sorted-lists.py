# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_cursor = list1
        result = list1
        
        while list1_cursor is not None:
            print(list1_cursor.val)
            
            list2_cursor = list2
            list1_next = list1_cursor.next
            print('===========')
            while list2_cursor is not None:
                print(list2_cursor.val)
                
                if list2_cursor.val < list1_cursor.val:
                    temp 
                
                list2_cursor = list2_cursor.next
            print('===========')
            
            list1_cursor = list1_next
        
        return ListNode(1, None)
    
solution = Solution()

list1 = ListNode(2, ListNode(4, ListNode(6, None)))
list2 = ListNode(1, ListNode(7, ListNode(9, None)))

print(solution.mergeTwoLists(list1, list2))