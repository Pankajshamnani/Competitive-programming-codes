import sys
import math
from collections import defaultdict
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

def power_factorization(n):
    prime_factors=defaultdict(lambda: 0)
    for i in range(2,int(math.sqrt(n))+1):
        while(n%i==0):
            prime_factors[i]+=1
            n=n//i
    if n>1:
        prime_factors[n]+=1
    return prime_factors


n=get_int()
print(factorization(n))

# for dictionary
ans=power_factorization(n)
product_of_all_factors=1
for i in ans:
    product_of_all_factors*=ans[i]+1
    print(i,ans[i])
#     total number of factors is the product of all (ans[i]+1)
print(product_of_all_factors)
