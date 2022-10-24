# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            self.root = TreeNode(value)

        else:
            self.rec_add(self.root, value)

    def rec_add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.rec_add(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.rec_add(node.right, value)

    def contains(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return False

        # if self.root.value == value:
        #     return True
        else:
            return self.rec_contains(value, self.root)

    def rec_contains(self, value, node):
        if node.value == value:
            return True
        elif node.value > value:
            if node.left is None:
                return False
            else:
                return self.rec_contains(value, node.left)
        else:
            if node.right is None:
                return False
            else:
                return self.rec_contains(value, node.right)

    def get_first(self) -> object:
        """
        TODO: Write this implementation
        """
        return self.root

    def remove_first(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return False

        if self.root.left is None:
            self.root = self.root.right
            return True
        elif self.root.right is None:
            self.root = self.root.left
            return True
        return self.rec_remove_first(self.root.right)

    def rec_remove_first(self, node):
        if node.left is None:
            node.left = self.root.left
            self.root = node
            return True

        elif node.left.left is None:
            temp = node.left.right
            node.left.left = self.root.left
            node.left.right = self.root.right
            self.root = node.left
            node.left = temp
            return True
        else:
            return self.rec_remove_first(node.left)

    def remove(self, value) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root.value == value:
            return self.remove_first()
        else:
            return self.rec_remove(value, None, self.root)

    def rec_remove(self, value, parent, node):
        if node.value > value:
            if node.left is None:
                return False
            else:
                return self.rec_remove(value, node, node.left)
        elif node.value < value:
            if node.right is None:
                return False
            else:
                return self.rec_remove(value, node, node.right)
        else:
            if node.right and node.left:
                successor = self.get_successor(node)
                successor.left = node.left
                successor.right = node.right
                if node == parent.left:
                    parent.left = successor
                else:
                    parent.right = successor
            elif node.right:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right
            elif node.left:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
            return True



    def pre_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        result = Queue()
        if self.root is None:
            return result

        self.rec_pre_order_traversal(self.root, result)

        return result

    def rec_pre_order_traversal(self, node, queue):

        queue.enqueue(node.value)
        if node.left:
            self.rec_pre_order_traversal(node.left, queue)
        if node.right:
            self.rec_pre_order_traversal(node.right, queue)

    def in_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        result = Queue()

        if self.root is None:
            return result

        self.rec_in_order_traversal(self.root, result)

        return result

    def rec_in_order_traversal(self, node, queue):
        if node.left:
            self.rec_in_order_traversal(node.left, queue)

        queue.enqueue(node.value)

        if node.right:
            self.rec_in_order_traversal(node.right, queue)

    def post_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        result = Queue()

        if self.root is None:
            return result

        self.rec_post_order_traversal(self.root, result)
        return result

    def rec_post_order_traversal(self, node, queue):

        if node.left:
            self.rec_post_order_traversal(node.left, queue)

        if node.right:
            self.rec_post_order_traversal(node.right, queue)

        queue.enqueue(node.value)

    def by_level_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        temp = Queue()
        result = Queue()

        if self.root is None:
            return result

        temp.enqueue(self.root)
        while not temp.is_empty():
            node = temp.dequeue()
            result.enqueue(node.value)
            if node.left:
                temp.enqueue(node.left)
            if node.right:
                temp.enqueue(node.right)

        return result



    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        if not self.root:
            return True

        return self.rec_is_full(self.root)

    def rec_is_full(self, node):
        if not node.left and not node.right:
            return True

        if node.left and not node.right or node.right and not node.left:
            return False

        if node.left and node.right:
            return self.rec_is_full(node.left) and self.rec_is_full(node.right)

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return True

        working_queue = Queue()
        working_queue.enqueue(self.root)
        found_end = False
        while not working_queue.is_empty():
            node = working_queue.dequeue()
            if node.left:
                if found_end:
                    return False
                working_queue.enqueue(node.left)
            else:
                found_end = True

            if node.right:
                if found_end:
                    return False
                working_queue.enqueue(node.right)
            else:
                found_end = True
        return True

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        if not self.root:
            return True

        else:
            height = self.height()
            return self.rec_is_perfect(self.root, height, 0)

    def rec_is_perfect(self, node, height, cur_height):
        if not node.left and not node.right:
            return height == cur_height
        elif node.left and not node.right:
            return False
        elif node.right and not node.left:
            return False
        else:
            return self.rec_is_perfect(node.left, height, cur_height+1)\
                   and self.rec_is_perfect(node.right, height, cur_height+1)



    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        if not self.root:
            return 0

        nodelist = self.in_order_traversal()
        count = 0
        while not nodelist.is_empty():
            nodelist.dequeue()
            count += 1
        return count

    def height(self) -> int:
        """
        TODO: Write this implementation
        """
        if not self.root:
            return -1
        else:
            return self.rec_height(self.root, 0)

    def rec_height(self, node, height):
        if not node.right and not node.left:
            return height

        elif node.right and not node.left:
            return self.rec_height(node.right, height+1)

        elif node.left and not node.right:
            return self.rec_height(node.left, height+1)

        else:
            lh = self.rec_height(node.left, height+1)
            rh = self.rec_height(node.right, height+1)
            if lh > rh:
                return lh
            else:
                return rh

    def count_leaves(self) -> int:
        """
        TODO: Write this implementation
        """
        if not self.root:
            return 0

        return self.rec_count_leaves(self.root)

    def rec_count_leaves(self, node):
        if not node.left and not node.right:
            return 1
        elif node.left and not node.right:
            return self.rec_count_leaves(node.left)
        elif node.right and not node.left:
            return self.rec_count_leaves(node.right)
        else:
            return self.rec_count_leaves(node.right) + self.rec_count_leaves(node.left)

    def count_unique(self) -> int:
        """
        TODO: Write this implementation
        """
        if not self.root:
            return 0

        nodelist = self.in_order_traversal()
        node = nodelist.dequeue()
        count = 1
        while not nodelist.is_empty():
            new_node = nodelist.dequeue()
            if node != new_node:
                count += 1
            node = new_node
        return count

    def get_successor(self, node):
        if node.right is None:
            return node.left
        elif node.left is None or node.right.left is None:
            return node.right
        else:
            return self.rec_get_successor(node.right)

    def rec_get_successor(self, node):
        if node.left.left is None:
            temp = node.left
            node.left = node.left.right
            return temp



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)

    """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)

    """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))

    """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))

    """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)

    """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))

    """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(20))
    # print(tree)

    """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree.remove(20))
    # print(tree)
    # # comment out the following lines
    # # if you have not yet implemented traversal methods
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove_first())
    # print(tree)

    """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.remove_first())
    # print(tree)

    """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

