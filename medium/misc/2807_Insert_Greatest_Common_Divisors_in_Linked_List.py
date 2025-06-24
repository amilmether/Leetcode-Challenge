# 2807. Insert Greatest Common Divisors in Linked List [Medium]
# Tags: misc

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        cur = head
        while cur.next:
            n1,n2 = cur.val,cur.next.val
            cur.next=ListNode(gcd(n1,n2),cur.next)
            cur=cur.next.next
        return head
        
        
