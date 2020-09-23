import sys
import math
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())

# code to check prime if number is prime limit=>10^^12 timecomplexity=>O(sqrt(n))
def isprime(n):
    if n==1:
        return 0
    s=math.sqrt(n)
    for i in range(2,int(s+1)):
        if  n%i==0:
            return 0
    return 1

# code to check prime numbers from 1 to n => limit:10^^6 timecomplexity=>O(nloglogn)
def sieve(n):
    prime=[True for i in range(n+1)]
    prime[0]=False
    prime[1]=False
    for i in range(2,n+1):
        if prime[i]==True:
            for j in range(i*i,n+1,i):
                prime[j]=False
    for i in range(len(prime)):
        if prime[i]==True:
            print(i)


