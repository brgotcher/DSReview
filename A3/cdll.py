# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        insert new node between sentinel and its 'next' node
        """
        new_node = DLNode(value)
        new_node.prev = self.sentinel
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        new_node.next.prev = new_node

    def add_back(self, value: object) -> None:
        """
        insert new node between sentinel and its 'prev' node
        """
        new_node = DLNode(value)
        new_node.next = self.sentinel
        new_node.prev = self.sentinel.prev
        self.sentinel.prev = new_node
        new_node.prev.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        insert new node at specified index
        """
        if index < 0 or index > self.length():
            raise CDLLException

        if index == 0:
            self.add_front(value)

        else:
            self.rec_insert_at_index(index, value, 0, self.sentinel.next)

    def rec_insert_at_index(self, index, value, current, node):
        if current == index - 1:
            new_node = DLNode(value)
            new_node.next = node.next
            new_node.prev = node
            node.next = new_node
            new_node.next.prev = new_node
        else:
            self.rec_insert_at_index(index, value, current+1, node.next)


    def remove_front(self) -> None:
        """
        remove the first node after the sentinel
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        remove the last node before the sentinel
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel

    def remove_at_index(self, index: int) -> None:
        """
        use a recursive helper to remove the node
        at the specified index
        """
        if index < 0 or index > self.length()-1:
            raise CDLLException

        if index == 0:
            self.remove_front()

        else:
            self.rec_remove_at_index(index, 0, self.sentinel.next)

    def rec_remove_at_index(self, index, current, node):
        if current == index - 1:
            node.next = node.next.next
            node.next.prev = node
        else:
            self.rec_remove_at_index(index, current+1, node.next)

    def get_front(self) -> object:
        """
        return the value of the first node after the sentinel
        """
        if self.is_empty():
            raise CDLLException

        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        return the value of the last node before the sentinel
        """
        if self.is_empty():
            raise CDLLException

        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        find and remove a node with the specified value
        if found and removed, return True, if not, return False
        """
        if self.is_empty():
            return False

        return self.rec_remove(value, self.sentinel.next)

    def rec_remove(self, value, node):
        if node.value == value:
            node.prev.next = node.next
            node.next.prev = node.prev
            return True
        elif node.next == self.sentinel:
            return False
        else:
            return self.rec_remove(value, node.next)

    def count(self, value: object) -> int:
        """
        count nodes in the list with the specified value
        """
        if self.is_empty():
            return 0

        return self.rec_count(value, self.sentinel.next, 0)

    def rec_count(self, value, node, count):
        if node == self.sentinel:
            return count

        if node.value == value:
            count += 1
        return self.rec_count(value, node.next, count)

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        """
        length = self.length()
        if index1 < 0 or index1 > length-1\
                or index2 < 0 or index2 > length-1:
            raise CDLLException

        if index1 == index2:
            return

        self.rec_swap_pairs(index1, index2, None, None, 0, self.sentinel.next)

    def rec_swap_pairs(self, index1, index2, node1, node2, current_index, current_node):
        if index1 == current_index:
            node1 = current_node
        if index2 == current_index:
            node2 = current_node

        if node1 is not None and node2 is not None:
            if abs(index1 - index2) > 1:
                temp = DLNode(0)
                temp.next = node2.next
                temp.prev = node2.prev
                node2.next = node1.next
                node2.prev = node1.prev
                node1.next = temp.next
                node1.prev = temp.prev
                node2.prev.next = node2
                node2.next.prev = node2
                node1.next.prev = node1
                node1.prev.next = node1
            else:
                if index1 > index2:
                    temp = node1
                    node1 = node2
                    node2 = temp
                node1.next = node2.next
                node2.prev = node1.prev
                node2.next = node1
                node1.prev = node2
                node1.next.prev = node1
                node2.prev.next = node2

        else:
            self.rec_swap_pairs(index1, index2, node1, node2, current_index+1, current_node.next)


    def reverse(self) -> None:
        """
        TODO: Write this implementation
        """
        length = self.length()
        if self.is_empty() or length == 1:
            return

        self.rec_reverse(self.sentinel.next, self.sentinel.prev, 0, length-1)

    def rec_reverse(self, node1, node2, index1, index2):
        if index1 >= index2:
            return

        if index2 - index1 == 1:
            node1.next = node2.next
            node2.prev = node1.prev
            node2.next = node1
            node1.prev = node2
            node1.next.prev = node1
            node2.prev.next = node2
            return
        else:
            temp = DLNode(0)
            temp.next = node2.next
            temp.prev = node2.prev
            node2.next = node1.next
            node2.prev = node1.prev
            node1.next = temp.next
            node1.prev = temp.prev
            node2.prev.next = node2
            node2.next.prev = node2
            node1.next.prev = node1
            node1.prev.next = node1
            self.rec_reverse(node2.next, node1.prev, index1+1, index2-1)

    def sort(self) -> None:
        """
        bubble sort
        """
        if self.is_empty():
            raise CDLLException
        if self.length() == 1:
            return

        self.rec_sort(self.sentinel.next, 0, self.sentinel)

    def rec_sort(self, low, low_index, high):
        if low.value > low.next.value:
            self.swap_pairs(low_index, low_index+1)
            low = low.prev

        if high != self.sentinel.next.next:
            if low.next.next == high:
                self.rec_sort(self.sentinel.next, 0, high.prev)
            else:
                self.rec_sort(low.next, low_index+1, high)

    def rotate(self, steps: int) -> None:
        if self.is_empty():
            return
        length = self.length()
        if length == 1:
            return
        while steps >= length:
            steps -= length
        while steps < 0:
            steps += length

        if steps == 0:
            return

        self.rec_rotate(self.sentinel.prev, 1, steps)

    def rec_rotate(self, node, current, steps):
        if current == steps:
            self.sentinel.prev.next = self.sentinel.next
            self.sentinel.next.prev = self.sentinel.prev
            self.sentinel.next = node
            self.sentinel.prev = node.prev
            node.prev.next = self.sentinel
            node.prev = self.sentinel

        else:
            self.rec_rotate(node.prev, current+1, steps)

    def remove_duplicates(self) -> None:
        """
        if a value appears more than once, remove all instances of that value
        """
        if self.is_empty():
            return

        self.rec_remove_duplicates(self.sentinel.next)

    def rec_remove_duplicates(self, node):
        if node.next == self.sentinel:
            return

        if node.value == node.next.value:
            while node.value == node.next.value:
                node.next = node.next.next
                node.next.prev = node
            node = node.prev
            node.next = node.next.next
            node.next.prev = node
        self.rec_remove_duplicates(node.next)

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            return
        length = self.length()
        if length < 3:
            return
        evens = CircularList()
        odds = CircularList()

        node = self.sentinel.next
        for i in range(1, length):
            if i % 2 == 0:
                evens.add_front(node)
            else:
                odds.add_front(node)
            node = node.next


    def add_integer(self, num: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)

    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)

    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)

    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)

    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())

    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)

    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    # print('\n# reverse example 1')
    # test_cases = (
    #     [1, 2, 3, 3, 4, 5],
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)

    # print('\n# reverse example 2')
    # lst = CircularList()
    # print(lst)
    # lst.reverse()
    # print(lst)
    # lst.add_back(2)
    # lst.add_back(3)
    # lst.add_front(1)
    # lst.reverse()
    # print(lst)

    # print('\n# reverse example 3')
    #
    #
    # class Student:
    #     def __init__(self, name, age):
    #         self.name, self.age = name, age
    #
    #     def __eq__(self, other):
    #         return self.age == other.age
    #
    #     def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)
    #
    #
    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)

    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)

    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)

    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)

    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)

    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)
    #
    # print('\n# odd_even example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], list('ABCDE'),
    #     [], [100], [100, 200], [100, 200, 300],
    #     [100, 200, 300, 400],
    #     [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)

    # print('\n# add_integer example 1')
    # test_cases = (
    #   ([1, 2, 3], 10456),
    #   ([], 25),
    #   ([2, 0, 9, 0, 7], 108),
    #    ([9, 9, 9], 9_999_999),
    #)
    # for list_content, integer in test_cases:
    #    lst = CircularList(list_content)
    # print('INPUT :', lst, 'INTEGER', integer)
    # lst.add_integer(integer)
    # print('OUTPUT:', lst)
