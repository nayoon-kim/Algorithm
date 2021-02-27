class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode):
    if l1 is None or l2 is None:
        return l1 if l2 is None else l2
        
    c = list()
    cur = l1
    cur2 = l2
    while cur2 != None and cur != None:
        if cur.val < cur2.val:
            print("cur.val insert ", cur.val)
            c.append(cur.val)
            cur = cur.next
        elif cur.val > cur2.val:
            print("cur2.val insert ", cur2.val)
            c.append(cur2.val)
            cur2 = cur2.next
        else:
            print("cur.val and cur2.val insert ", cur.val, cur2.val)
            c.append(cur.val)
            c.append(cur2.val)
            cur = cur.next
            cur2 = cur2.next

    if cur != None:
        _a = cur
        while _a != None:
            c.append(_a.val)
            _a = _a.next
    if cur2 != None:
        _a = cur2
        while _a != None:
            c.append(_a.val)
            _a = _a.next
        
    a = ListNode()
        
    for i in c:
        if a.val == 0:
            a = ListNode(i)
        else:
            k = a
            while k.next != None:
                k = k.next
            k.next = ListNode(i)
    if a.val == None:
        a = ListNode('')
    
    return a

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print(mergeTwoLists(l1, l2))