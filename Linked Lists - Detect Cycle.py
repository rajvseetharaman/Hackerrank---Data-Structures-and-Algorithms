"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    current=head
    while current.next!=None:
        current=current.next
        checkloop=current
        while checkloop.next!=None:
            checkloop=checkloop.next
            if checkloop==current:
                return True
    return False
    
