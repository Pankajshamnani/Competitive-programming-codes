import sys
import math
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd(18,36))
