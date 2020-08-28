class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None


def mergeTwoLists( l1, l2):
    out = l3 = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            l3.next = ListNode(l1.val)
            l3 = l3.next
            l1 = l1.next
        else:
            l3.next = ListNode(l2.val)
            l3 = l3.next
            l2 = l2.next
    while l1:
        l3.next = l1
        l3 = l3.next
        l1 = l1.next
    while l2:
        l3.next = l2
        l3 = l3.next
        l2 = l2.next

    return out.next