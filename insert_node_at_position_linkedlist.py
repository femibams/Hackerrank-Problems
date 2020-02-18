def insertNodeAtPosition(head, data, position):
    data = SinglyLinkedListNode(data)
    if head is None:
        head = data
        return head
    
    if position == 0:
        temp = head
        head = data
        head.next = temp

    curr = head
    for i in range(position):
        previous = curr
        curr = curr.next
        if i == (position - 1):
            previous.next = data
            data.next = curr
            return head
