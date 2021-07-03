'''Megrging k sorted lists using recursion'''


def KsortedLists(lists):
    if not lists:
        return None

    if len(lists)==1:
        return lists[0]

    mid = len(lists)//2
    left = KsortedLists(lists[:mid])
    right = KsortedLists(lists[mid:])

    return merge(left,right)


def merge(l1,l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    return dummy.next