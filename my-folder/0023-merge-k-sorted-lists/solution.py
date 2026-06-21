# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finallist=[]
        for head in lists:
                current = head
                while current:
                    finallist.append(current.val)
                    current = current.next
        
        finallist = sorted(finallist)
        
        dummy = ListNode(0)
        current = dummy
        for ele in finallist:
            current.next = ListNode(ele)
            current = current.next
        
        return dummy.next
            


       
