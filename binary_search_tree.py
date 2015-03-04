#!/bin/env python2
#  
#  Some functions are aased on:
#  Binary Search Tree
#  Efficient Searching using BinaryArraySearch and Binary Search Trees Part 1
#  By: George T. Heineman
#  Publisher: O'Reilly Media, Inc.
#

import random
from time import time

class BinaryNode:

    def __init__(self, value = None):
        ''' Creates an empty BinaryNode '''
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        ''' Adds new value to Binary Node '''
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)


class BinaryTree:

    def __init__(self):
        ''' Create an empty tree '''
        self.root = None

    def add(self, value):
        ''' Adds new value to Binary Tree '''
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        ''' Search for target in BinaryTree'''
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right

        return False


def deepest_node(node):
    ''' Gets the deepest node in the tree '''
    deepest = None
    if node:
        queue = []
        queue.insert(0,node)
        while (queue):
            node = queue.pop()
            deepest = node.value
            if node.left:
                queue.insert(0,node.left)
            if node.right:
                queue.insert(0,node.right)
    return deepest
    
def pre_order(node):
    ''' Pre-Order implementation '''
    if not node:
        return
    print (node.value)
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    ''' In-Order Implementation '''
    if not node:
        return
    in_order(node.left)
    print (node.value)
    in_order(node.right)

def post_order(node):
    ''' Post-Order Implementation '''
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print (node.value)
    
def performance():
    ''' Mesures performance of certain function'''
    n = 1024
    while n < 65536:
        
        bt = BinaryTree()
    for i in range(n):
        bt.add(random.randint(1,n))
            
        now = time()
        bt.contains(random.randint(1,n))
        print (n, (time() - now))
        
        n*= 2
