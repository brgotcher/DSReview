# Course: CS261 - Data Structures
# Assignment: 5
# Student:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        index = self.heap.length()
        self.heap.append(node)
        if index > 0:
            child = node
            parent_index = (index-1)//2
            parent = self.heap[parent_index]
            while parent and child < parent:
                self.heap.swap(index, parent_index)
                index = parent_index
                if index == 0:
                    parent = None
                else:
                    parent_index = (index-1)//2
                    parent = self.heap[parent_index]

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException

        return self.heap[0]

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException

        if self.heap.length() == 1:
            return self.heap.pop()

        removed = self.heap[0]
        length = self.heap.length()
        perc = self.heap.pop()
        self.heap[0] = perc
        perc_index = 0
        left = 1
        right = 2
        while right < length-1 and (perc > self.heap[left] or perc > self.heap[right]):
            if self.heap[left] <= self.heap[right]:
                self.heap.swap(perc_index, left)
                perc_index = left
                left = perc_index*2+1
                right = left+1
            else:
                self.heap.swap(perc_index, right)
                perc_index = right
                left = perc_index*2+1
                right = left+1
        if left < length-1 and perc > self.heap[left]:
            self.heap.swap(perc_index, left)
        return removed




    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        length = da.length()
        self.heap = DynamicArray()
        for i in range(length):
            self.heap.append(da[i])

        for i in range((length-1)//2, -1, -1):
            parent_index = i
            left_index = i*2+1
            right_index = left_index+1
            if right_index < length:
                left = self.heap[left_index]
                right = self.heap[right_index]
                if left <= right:
                    min_child_index = left_index
                else:
                    min_child_index = right_index
            elif left_index < length:
                min_child_index = left_index
            else:
                min_child_index = parent_index
            if self.heap[min_child_index] < self.heap[parent_index]:
                self.heap.swap(min_child_index, parent_index)





# BASIC TESTING
if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)


    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())


    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
