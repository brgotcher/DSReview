# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        new_node = SLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        # traverse the list to find last node
        if self.head.next == self.tail:
            self.add_front(value)

        else:
            self.rec_add_back(value, self.head)

    def rec_add_back(self, value, node):
        if node.next == self.tail:
            new_node = SLNode(value)
            node.next = new_node
            new_node.next = self.tail
        else:
            self.rec_add_back(value, node.next)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0:
            raise SLLException

        if index == 0:
            self.add_front(value)
        else:
            self.rec_insert_at_index(index, value, 0, self.head.next)

    def rec_insert_at_index(self, index, value, current, node):
        if index == current+1:
            new_node = SLNode(value)
            new_node.next = node.next
            node.next = new_node
        elif node.next == self.tail:
            raise SLLException
        else:
            self.rec_insert_at_index(index, value, current+1, node.next)

    def remove_front(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.head.next == self.tail:
            raise SLLException

        self.head.next = self.head.next.next

    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.head.next == self.tail:
            raise SLLException

        self.rec_remove_back(self.head)

    def rec_remove_back(self, node):
        if node.next.next == self.tail:
            node.next = self.tail
        else:
            self.rec_remove_back(node.next)

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or self.head.next == self.tail:
            raise SLLException

        if index == 0:
            self.head.next = self.head.next.next

        else:
            self.rec_remove_at_index(index, self.head.next, 0)

    def rec_remove_at_index(self, index, node, current):
        if node.next == self.tail:
            raise SLLException

        if index == current+1:
            node.next = node.next.next
        else:
            self.rec_remove_at_index(index, node.next, current+1)

    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.head.next == self.tail:
            raise SLLException

        return self.head.next.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.head.next == self.tail:
            raise SLLException

        if self.head.next.next == self.tail:
            return self.head.next.value

        return self.rec_get_back(self.head.next)

    def rec_get_back(self, node):
        if node.next == self.tail:
            return node.value
        else:
            return self.rec_get_back(node.next)

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self.head.next == self.tail:
            return False

        return self.rec_remove(value, self.head)

    def rec_remove(self, value, node):
        if node.next == self.tail:
            return False

        if node.next.value == value:
            node.next = node.next.next
            return True
        else:
            return self.rec_remove(value, node.next)

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        if self.head.next == self.tail:
            return 0

        return self.rec_count(value, self.head.next, 0)

    def rec_count(self, value, node, count):
        if node.value == value:
            count += 1

        if node.next == self.tail:
            return count
        else:
            return self.rec_count(value, node.next, count)

    def slice(self, start_index: int, size: int) -> object:
        """
        TODO: Write this implementation
        """
        if start_index < 0 or start_index + size > self.length():
            raise SLLException

        if size == 0:
            return LinkedList()

        return self.rec_slice(start_index, size, self.head.next, 0, LinkedList())

    def rec_slice(self, start_index, size, node, current, output):
        if current == start_index + (size-1):
            output.add_back(node.value)
            return output

        if start_index <= current < start_index + size:
            output.add_back(node.value)

        return self.rec_slice(start_index, size, node.next, current+1, output)



if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)


    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)


    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))


    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))


    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)


    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)


    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))


    # print('\n# get_back example 1')
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())


    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)


    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

