import pytest
from MyLinkedList import LinkedList

class TestLinkedList:

    @pytest.fixture
    def empty(self) -> LinkedList:
        return LinkedList()
    
    @pytest.fixture
    def linked_list(self) -> LinkedList:
        return LinkedList.from_sequence([0, 1, 2, 3, 4])

    def test_append(self, empty: LinkedList) -> None:
        empty.append(1)
        assert len(empty) == 1
        assert empty.tail.data == 1

    def test_prepend(self, empty: LinkedList) -> None:
        empty.prepend(1)
        assert len(empty) == 1
        assert empty.head.data == 1

    def test_insert_before(self, linked_list: LinkedList) -> None:
        linked_list.find(2).add_before(99)
        assert 99 in linked_list
        assert linked_list.to_list() == [0, 1, 99, 2, 3, 4]

    def test_insert_before_not_found(self, linked_list: LinkedList) -> None:
        with pytest.raises(ValueError):
            linked_list.find(10).add_before(99)

    def test_insert_after(self, linked_list: LinkedList) -> None:
        linked_list.find(2).add_after(99)
        assert 99 in linked_list
        assert linked_list.to_list() == [0, 1, 2, 99, 3, 4]

    def test_insert_after_not_found(self, linked_list: LinkedList) -> None:
        with pytest.raises(ValueError):
            linked_list.find(10).add_after(99)

    def test_remove(self, linked_list: LinkedList) -> None:
        linked_list.find(2).remove()
        assert 2 not in linked_list
        assert linked_list.to_list() == [0, 1, 3, 4]

    def test_remove_not_found(self, linked_list: LinkedList) -> None:
        with pytest.raises(ValueError):
            linked_list.find(10).remove()

    def test_remove_all(self, linked_list: LinkedList) -> None:
        linked_list.append(2)
        for node in linked_list.find_all(2):
            node.remove()
        assert 2 not in linked_list
        assert linked_list.to_list() == [0, 1, 3, 4]

    def test_pop(self, linked_list: LinkedList) -> None:
        assert linked_list.pop() == 4
        assert len(linked_list) == 4

    def test_pop_empty(self, empty: LinkedList) -> None:
        with pytest.raises(IndexError):
            empty.pop()

    def test_pop_front(self, linked_list: LinkedList) -> None:
        assert linked_list.pop_front() == 0
        assert len(linked_list) == 4

    def test_pop_front_empty(self, empty: LinkedList) -> None:
        with pytest.raises(IndexError):
            empty.pop_front()

    def test_front(self, linked_list: LinkedList) -> None:
        assert linked_list.head.data == 0

    def test_front_empty(self, empty: LinkedList) -> None:
        with pytest.raises(Exception):
            _ = empty.head.data

    def test_back(self, linked_list: LinkedList) -> None:
        assert linked_list.tail.data == 4

    def test_back_empty(self, empty: LinkedList) -> None:
        with pytest.raises(Exception):
            _ = empty.tail.data

    def test_empty(self, empty: LinkedList, linked_list: LinkedList) -> None:
        assert empty.empty is True
        assert linked_list.empty is False

    def test_len(self, empty: LinkedList, linked_list: LinkedList) -> None:
        assert len(empty) == 0
        assert len(linked_list) == 5

    def test_clear(self, linked_list: LinkedList) -> None:
        linked_list.clear()
        assert len(linked_list) == 0
        assert linked_list.empty is True

    def test_contains(self, linked_list: LinkedList) -> None:
        assert 2 in linked_list
        assert 10 not in linked_list

    def test_iter(self, linked_list: LinkedList) -> None:
        assert [node.data for node in list(iter(linked_list))] == [0, 1, 2, 3, 4]

    def test_eq(self, linked_list: LinkedList) -> None:
        other = LinkedList.from_sequence([0, 1, 2, 3, 4])
        assert linked_list == other
        other.append(5)
        assert linked_list != other

    def test_reversed(self, linked_list: LinkedList) -> None:
        reversed_list = list(reversed(linked_list))
        assert reversed_list == [4, 3, 2, 1, 0]
    
    #I'm not restricting my linked list to a single type, since there's no cost to allowing mixed types in a linked list
    #def test_check_type_asserts(self, linked_list: LinkedList) -> None:
    #    with pytest.raises(TypeError):
    #        linked_list.append("string")
    #    with pytest.raises(TypeError):
    #        linked_list.prepend("string")
    #    with pytest.raises(TypeError):
    #        linked_list.find(1).add_after("string")
    #    with pytest.raises(TypeError):
    #        linked_list.find(1).add_before("string")
    #    with pytest.raises(TypeError):
    #        linked_list.find("string").add_after(2)
    #    with pytest.raises(TypeError):
    #        linked_list.find("string").add_before(2)
    #    with pytest.raises(TypeError):
    #        linked_list.find("string").remove("string")
    #    with pytest.raises(TypeError):
    #        for node in linked_list.find_all("string"):
    #            node.remove()
    #    with pytest.raises(TypeError):
    #        LinkedList.from_sequence([1, 2, 3])

    def test_value_error_raised(self, linked_list: LinkedList) -> None:
        with pytest.raises(ValueError):
            linked_list.find(10).add_before(99)  # Target not in list
        with pytest.raises(ValueError):
            linked_list.find(10).add_after(99)  # Target not in list
        with pytest.raises(ValueError):
            linked_list.find(10).remove()  # Item not in list