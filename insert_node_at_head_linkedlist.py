def insertNodeAtHead(llist, data):
    head = llist
    # Write your code here
    if head == None:
        head = SinglyLinkedListNode(data)
        return head

    temp = head
    head = SinglyLinkedListNode(data)
    head.next = temp
    return head