from typing import Optional, Sequence, Any
import os

class LinkedList:

    class Node:
        def __init__(self, parent, data):
            self.__data: Any = data
            self.__parent: LinkedList = parent
            self.__next: Optional[LinkedList.Node] = None
            self.__previous: Optional[LinkedList.Node] = None
        
        @property
        def data(self) -> Any:
            return self.__data
        
        @data.setter
        def data(self, data):
            self.__data = data
        
        @property
        def next(self):
            return self.__next
        
        @property
        def previous(self):
            return self.__previous
        
        @property
        def parent(self):
            return self.__parent
        
        def add_after(self, data):
            """
            add a new node after this node
            """
            new_node = LinkedList.Node(self.parent, data)
            if self.next is None:
                self.parent._LinkedList__tail = new_node
            else:
                self.next.__previous = new_node
                new_node.__next = self.next

            new_node.__previous = self
            self.__next = new_node
            self.parent._LinkedList__count += 1
        
        def add_before(self, data):
            """
            add a new node before this node
            """
            new_node = LinkedList.Node(self.parent, data)
            if self.previous is None:
                self.parent._LinkedList__head = new_node
            else:
                self.previous.__next = new_node
                new_node.__previous = self.next

            new_node.__next = self
            self.__previous = new_node
            self.parent._LinkedList__count += 1
        
        def remove(self):
            """
            remove this node from the chain
            node will continue existing temporarily, but will no longer be referenced by adjacent nodes
            """
            if self.next is None:
                self.parent._LinkedList__tail = self.previous
            else:
                self.next.__previous = self.previous

            if self.previous is None:
                self.parent._LinkedList__head = self.next
            else:
                self.previous.__next = self.next
            
            self.parent._LinkedList__count -= 1

        def __str__(self) -> str:
            return str(self.data)

        def __repr__(self) -> str:
            return str(self.previous) + "<->" + str(self) + "<->" + str(self.next)

    def __init__(self):
        self.__head: Optional[LinkedList.Node] = None
        self.__tail: Optional[LinkedList.Node] = None
        self.__count = 0
    
    @staticmethod
    def from_sequence(sequence: Sequence):
        outputList = LinkedList()
        for item in sequence:
            outputList.append(item)
        
        return outputList
    
    def append(self, item) -> None:
        if self.empty:
            self.__add_first(item)
        else:
            self.tail.add_after(item)
    
    def prepend(self, item) -> None:
        if self.empty:
            self.__add_first(item)
        else:
            self.head.add_before(item)
    
    def __add_first(self, item):
        """
        internal helper function to add the first element to an empty list
        """
        if not self.empty:
            raise IndexError("attempted to add the first element to a non empty list, something's wrong")
        new_node: LinkedList.Node = LinkedList.Node(self, item)
        self.__head = self.__tail = new_node
        self.__count += 1

    def pop(self) -> Any:
        if self.empty:
            raise IndexError("attempted to pop from empty list")
        out = self.tail.data
        self.__tail = self.tail.previous
        if self.tail is None:
            self.__head = None
        else:
            self.tail.__next = None
        self.__count -= 1
        return out
    
    def pop_front(self) -> Any:
        if self.empty:
            raise IndexError("attempted to pop from empty list")
        out = self.head.data
        self.__head = self.head.next
        if self.head is None:
            self.__tail = None
        else:
            self.head.__previous = None
        self.__count -= 1
        return out
    
    def find(self, item) -> "LinkedList.Node":
        for node in self:
            if node.data == item:
                return node
        raise ValueError("item not found")

    def find_all(self, item) -> list["LinkedList.Node"]:
        out = []
        for node in self:
            if node.data == item:
                out.append(node)
        return out
    
    def to_list(self) -> list[Any]:
        return [node.data for node in self]

    @property
    def head(self) -> "LinkedList.Node":
        return self.__head

    @property
    def tail(self) -> "LinkedList.Node":
        return self.__tail
    
    @property
    def empty(self) -> bool:
        return len(self) == 0
    
    def __len__(self) -> int:
        return self.__count
    
    def clear(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    def __contains__(self, item) -> bool:
        for node in self:
            if node.data == item:
                return True
        return False
    
    def __iter__(self) -> "LinkedList":
        self.__travel_node = self.head
        return self

    def __next__(self) -> "LinkedList.Node":
        if self.__travel_node is None:
            raise StopIteration
        
        out = self.__travel_node
        self.__travel_node = self.__travel_node.next
        return out
    
    def __reversed__(self) -> "LinkedList":
        #idk how to implement reversed in a class that's implemented next
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        for node1, node2 in zip(self, other):
            if node1.data != node2.data:
                return False
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'
    
    def __repr__(self) -> str:
        items = []
        current = self.__head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.__count}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')