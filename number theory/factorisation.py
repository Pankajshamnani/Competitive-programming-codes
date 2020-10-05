import sys
import math
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())

def factorization(n):
    prime_factors=[]
    for i in range(2,int(math.sqrt(n))+1):
        while(n%i==0):
            prime_factors.append(i)
            n=n//i
    if n>1:
        prime_factors.append(n)
    return prime_factors


n=get_int()
print(factorization(n))
