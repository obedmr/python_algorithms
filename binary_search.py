#!/bin/env python2
#  
#  Based on:
#  Working with Algorithms in Python
#  Efficient Searching using BinaryArraySearch and Binary Search Trees Part 1
#  By: George T. Heineman
#  Publisher: O'Reilly Media, Inc.
#

From Time import time

def contains(collection, target):
    ''' Python function for searching a target in collection '''
    return target in collection

def binary_search(collection, target):
    ''' Binary Search Algorithm  '''
    low = 0
    high = len(collection) - 1

    while low <= high:
        middle = (low + high) / 2
        if target == collection[middle]:
            return middle
        elif target < collection[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -(low + 1)

def insert_in_place(ordered_collection, target):
    ''' Insert target into teh proper location '''

    for i in range(len(ordered_collection)):
        if target < ordered_collection[i]:
            ordered_collection.insert(i, target)
            return
    ordered_collection.append(target)

def insert_in_place_optimized(ordered_collection, target):
    ''' Optimized Insert in Place with Binary Search Algorithm '''
    index = binary_search(ordered_collection,target)
    if index < 0:
        ordered_collection.insert(-(index + 1),target)
        return 
    ordeted_collection.insert(index, target)
    
def performance(function):
    ''' Mesures execution time for a certain search function '''
    num_elements = 1024
    while num_elements < 50000000:
        sorted = range(num_elements)
        now = time()
        # Code whose performance is to be evaluated
        function(sorted,  len(sorted) + 1)
        done = time()

        print(num_elements, (done-now)*1000)
        num_elements *= 2
