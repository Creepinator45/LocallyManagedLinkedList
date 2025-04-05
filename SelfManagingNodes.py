from typing import Optional, Any

class Node:
    def __init__(self, data):
        self.__data: Any = data
        self.__next: Optional[Node] = None
        self.__previous: Optional[Node] = None
    
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

    def add_after(self, data):
        """
        add a new node after this node
        """
        new_node = Node(data)
        if self.next is not None:
            self.next.__previous = new_node
            new_node.__next = self.next
        new_node.__previous = self
        self.__next = new_node
    
    def add_before(self, data):
        """
        add a new node before this node
        """
        new_node = Node(data)
        if self.previous is not None:
            self.previous.__next = new_node
            new_node.__previous = self.previous
        new_node.__next = self
        self.__previous = new_node
    
    def remove(self):
        """
        remove this node from the chain
        node will continue existing temporarily, but will no longer be referenced by adjacent nodes
        """
        if self.next is not None:
            self.next.__previous = self.previous
        if self.previous is not None:
            self.previous.__next = self.next
    
    def find_head(self) -> "Node":
        """
        traverse to and return the first node
        O(n)
        """
        working_node = self
        while working_node.previous is not None:
            working_node = working_node.previous

        return working_node