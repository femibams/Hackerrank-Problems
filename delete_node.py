def deleteNode(head, position):
    curr = head
    if position == 0:
        head = head.next
        return head

    for i in range(position):
        previous = curr
        curr = curr.next
        if i == (position - 1):
            previous.next = curr.next
            return head
