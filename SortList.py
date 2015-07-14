# Sort a linked list in O(n log n) time using constant space complexity.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        n = self.next
        s = []
        s.append(self.val)
        while n is not None:
            s.append( n.val)
            n = n.next
        return str(s)

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        def move( list, step):
            while list is not None and step > 0:
                list = list.next
                step = step - 1
            return list

        def merge( list, length):
            if list is None or list.next is None:
                return None

            leftStart = list.next
            leftEnd = move( leftStart, length/2 -1)
            if leftEnd is None:
                return None

            rightStart = leftEnd.next
            leftEnd.next = None
            rightEnd = move( rightStart, length/2 -1)
            if rightEnd is None:
                rightEndNext = None
            else:
                rightEndNext = rightEnd.next
                rightEnd.next = None

            while leftStart is not None or rightStart is not None:
                if rightStart is None or ( leftStart is not None and leftStart.val < rightStart.val):
                    list.next = leftStart
                    leftStart = leftStart.next
                    list = list.next
                else:
                    list.next = rightStart
                    rightStart = rightStart.next
                    list = list.next
            list.next = rightEndNext
            return list

        if head is None or head.next is None:
            return head
        k = 1
        dummy = ListNode(0)
        dummy.next = head
        nMerges = 2
        while nMerges > 1:
            k = k*2
            list = dummy
            nMerges = 0
            while list is not None and list.next is not None:
                list = merge( list, k)
                nMerges = nMerges + 1
        return dummy.next


if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(1)
    #a.next.next = ListNode(1)
    #a.next.next.next = ListNode(4)
    print Solution().sortList(a)
