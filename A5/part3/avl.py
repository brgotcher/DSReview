# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

import random

from bst import BST
from bst import TreeNode
from bst import Stack
from bst import Queue


class AVLTreeNode(TreeNode):
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None
        self.height = 0


class AVL(BST):
    def add(self, value):
        """
        TODO: Write your implementation
        """
        if self.root is None:
            self.root = AVLTreeNode(value)

        node = self.rec_add(value, self.root)
        if node:
            self.balance(node)

    def rec_add(self, value, node):
        if value < node.value:
            if node.left:
                return self.rec_add(value, node.left)
            else:
                node.left = AVLTreeNode(value)
                node.left.parent = node
                self.increment_heights(node)
                return node
        elif value > node.value:
            if node.right:
                return self.rec_add(value, node.right)
            else:
                node.right = AVLTreeNode(value)
                node.right.parent = node
                self.increment_heights(node)
                return node
        else:
            return None

    def remove(self, value) -> bool:
        """
        TODO: Write your implementation
        """
        if not self.root:
            return False

        return self.rec_remove(value, self.root)

    def rec_remove(self, value, node) -> bool:
        if node.value == value:
            successor = self.get_successor(node)
            if not successor:
                if node.parent and node.parent.left == node:
                    node.parent.left = None
                    self.balance(node.parent)
                    return True
                elif node.parent and node.parent.right == node:
                    node.parent.right = None
                    self.balance(node.parent)
                    return True
                else:
                    self.root = None
                    return True
            if node.left != successor:
                successor.left = node.left
                if node.left:
                    node.left.parent = successor
            # else:
            #     successor.left = None
            if node.right != successor:
                successor.right = node.right
                if node.right:
                    node.right.parent = successor
            # else:
            #     successor.right = None
            successor.parent = node.parent
            if successor.parent and successor.parent.left == node:
                successor.parent.left = successor
            elif successor.parent and successor.parent.right == node:
                successor.parent.right = successor
            if self.root == node:
                self.root = successor
            self.balance(successor)
            return True

        elif value < node.value:
            if node.left:
                return self.rec_remove(value, node.left)
            else:
                return False
        else:
            if node.right:
                return self.rec_remove(value, node.right)
            else:
                return False

    def increment_heights(self, node):
        if node.right and node.left:
            if node.right.height >= node.left.height:
                node.height = node.right.height + 1
            else:
                node.height = node.left.height + 1
        elif node.right:
            node.height = node.right.height + 1
        elif node.left:
            node.height = node.left.height + 1
        else:
            node.height = 0

        if node.parent:
            self.increment_heights(node.parent)

    def get_balance_factor(self, node):
        if node.left and node.right:
            return node.right.height - node.left.height
        elif node.left:
            return -1 - node.left.height
        elif node.right:
            return 1 + node.right.height
        else:
            return 0

    def balance(self, node):
        balance_factor = self.get_balance_factor(node)
        if balance_factor < -1:
            if self.get_balance_factor(node.left) <= 0:
                self.right_rotation(node)
            else:
                self.left_right_rotation(node)
        elif balance_factor > 1:
            if self.get_balance_factor(node.right) >= 0:
                self.left_rotation(node)
            else:
                self.right_left_rotation(node)

        if node.parent:
            self.balance(node.parent)

    def left_rotation(self, node):
        parent = node.parent
        child = node.right
        if parent and parent.left == node:
            parent.left = child
        elif parent and parent.right == node:
            parent.right = child
        else:
            self.root = child
        # child.left = node
        child.parent = parent
        node.parent = child
        node.right = child.left
        if node.right:
            node.right.parent = node

        child.left = node
        self.increment_heights(node)

    def right_rotation(self, node):
        parent = node.parent
        child = node.left
        if parent and parent.left == node:
            parent.left = child
        elif parent and parent.right == node:
            parent.right = child
        else:
            self.root = child
        # child.right = node
        child.parent = parent
        node.parent = child
        node.left = child.right
        if node.left:
            node.left.parent = node

        child.right = node
        self.increment_heights(node)

    def right_left_rotation(self, node):
        self.right_rotation(node.right)
        self.left_rotation(node)

    def left_right_rotation(self, node):
        self.left_rotation(node.left)
        self.right_rotation(node)

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
            if node.left:
                self.balance(node.left)
            else:
                self.balance(node)
            return temp
        else:
            return self.rec_get_successor(node.left)


if __name__ == '__main__':

    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # test_cases = (
    #     (1, 2, 3),          #RR
    #     (3, 2, 1),          #LL
    #     (1, 3, 2),          #RL
    #     (3, 1, 2),          #LR
    # )
    #
    # for case in test_cases:
    #     avl = AVL(case)
    #     print(avl)
    #
    #
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # test_cases = (
    #     (10, 20, 30, 40, 50),   # RR, RR
    #     (10, 30, 30, 50, 40),   # RR, RL
    #     (30, 20, 10, 5, 1),     # LL, LL
    #     (30, 20, 10, 1, 5),     # LL, LR
    #     (5, 4, 6, 3, 7, 2, 8),  # LL, RR
    #     (range(0, 30, 3)),
    #     (range(0, 31, 3)),
    #     (range(0, 34, 3)),
    #     (range(10, -10, -2)),
    #     ('A', 'B', 'C', 'D', 'E'),
    #     (1, 1, 1, 1),
    # )
    # for case in test_cases:
    #     avl = AVL(case)
    #     print('INPUT  :', case)
    #     print('RESULT :', avl)

    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # test_cases = (
    #     ((1, 2, 3), 1),  # no AVL rotation
    #     ((1, 2, 3), 2),  # no AVL rotation
    #     ((1, 2, 3), 3),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    #
    #
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # avl = AVL(case)
    # for del_value in case:
    #     print('INPUT  :', avl, del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)


    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # avl = AVL(case)
    # for _ in case[:-2]:
    #     print('INPUT  :', avl.size(), avl, avl.root)
    #     avl.remove(avl.root.value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     avl = AVL(case)
    #     if avl.size() != len(case):
    #         raise Exception("PROBLEM WITH ADD OPERATION")
    #     for value in case[::2]:
    #         avl.remove(value)
    #     if avl.size() != len(case) - len(case[::2]):
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('Stress test finished')

    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = AVL()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())


    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = AVL()
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
