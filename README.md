
# LinkedLists

These are a couple of custom Linked List implementations

## Files

SelfManagingNodes.py implements a linked list using purely self managed nodes, that only have information about their adjacent nodes, with no higher level linked list container. I find this implementation mathematically satisfying, but it would be impractical for most situations.

MyLinkedList.py is an implementation that was designed to mirror a linked list implementation for my computer science class, but that makes use of more self sufficient nodes that can be safely given to an end user.

test_linkedlist.py is the the test file from my computer science class, but modified to fit with my custom linklist syntactically.