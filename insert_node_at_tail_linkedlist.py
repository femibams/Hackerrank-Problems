def insertNodeAtTail(head, data):
    if head == None:
        head = SinglyLinkedListNode(data)
        return head
    
    current = head
    while current.next != None:
        current = current.next
    
    current.next = SinglyLinkedListNode(data)
    return head