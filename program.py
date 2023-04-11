import sys
sys.setrecursionlimit(10**6)
import random
import time
import copy
from binary_search import binary_search
from quick_sort import quicksort

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def get_height(root):
    if root is None:
        return 0
    else:
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        return max(left_height, right_height) + 1

def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

CB = 0
CTA = 0
CTB = 0

SA = 0
SB = 0
STA = 0
STB = 0

hTA = 0
hTB = 0

value = 5000

A = [i+1 for i in range(value)]
random.shuffle(A)

start_time = time.perf_counter()
B = copy.deepcopy(A)
sorted_B = quicksort(B)
end_time = time.perf_counter()
CB = end_time - start_time

start_time = time.perf_counter()
root_TA = None
for item in A:
    root_TA = insert(root_TA, item)
end_time = time.perf_counter()
CTA = end_time - start_time
hTA = get_height(root_TA)

start_time = time.perf_counter()
root_TB = sorted_array_to_bst(B)
end_time = time.perf_counter()
CTB = end_time - start_time
hTB = get_height(root_TB)

start_time = time.perf_counter()
for i in B:
    for j in A:
        if i == j:
            break
end_time = time.perf_counter()
SA = end_time - start_time
 
start_time = time.perf_counter()
binary_search(A, B)
end_time = time.perf_counter()
SB = end_time - start_time

start_time = time.perf_counter()
for item in A:
    result = search(root_TA, item)
end_time = time.perf_counter()
STA = end_time - start_time

start_time = time.perf_counter()
for item in A:
    result = search(root_TB, item)
end_time = time.perf_counter()
STB = end_time - start_time

print(f"n: ", value)
print(f"CB: ", CB)
print(f"CTA : ", CTA )
print(f"CTB : ", CTB )
print(f"SA : ", SA )
print(f"SB : ", SB )
print(f"STA : ", STA )
print(f"STB : ", STB )
print(f"hTA  : ", hTA  )
print(f"hTB : ", hTB )
