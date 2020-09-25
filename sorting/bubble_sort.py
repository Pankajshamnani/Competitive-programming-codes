import sys
import math
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())

#time complexity=O(n*n)
def bubble_sort_asc(a):
    for i in range(len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

#time complexity=O(n*n)
def bubble_sort_desc(a):
    for i in range(len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[4,2,67,24,123,52,1,24,534]
print(bubble_sort_desc(a))

