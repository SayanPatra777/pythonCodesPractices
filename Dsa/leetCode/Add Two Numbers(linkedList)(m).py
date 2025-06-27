# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        count1,count2=0,0
        num1,num2=0,0
        while l1 or l2:
            if l1:
                num1+=l1.val*(pow(10,count1))
                count1+=1
                l1=l1.next
            if l2:
                num2+=l2.val*(pow(10,count2))
                count2+=1
                l2=l2.next
        sums=num1+num2
        if sums == 0:
            return ListNode(0)
        head = None
        current = None
        while sums:
            rem = sums % 10
            sums //= 10
            new_node = ListNode(rem)
            if not head:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next
        return head

''' here I've used 2 loops but code is passed in O(n) time complexity
 and O(1) space complexity
 where n is the number of nodes in the linked list
 the second loop that is used to create the new linked list, I took a little help from ChatGPT
 '''
