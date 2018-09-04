# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import time
import math


def issimple(a):
    r = math.ceil(math.sqrt(a))
    r = int(r)
    lst = []
    for i in range(3, r):
        if a % i == 0:
            if issimple(i) == []:
                lst.append(i)
    return lst


def ssp(a):
    r = math.ceil(math.sqrt(a))
    r = int(r)
    lst = []
    for i in range(3, r):
        if a % i == 0:
            if issimple(i) == []:
                print(i, r)
                lst.append(i)
    return lst


t1 = time.time()
print("          UNO")
r = issimple(600851475143)
print(r)
print(time.time() - t1)
print(max(r))

t1 = time.time()
print("          DOS")
r = ssp(600851475143)
print(r)
print(time.time() - t1)
print(max(r))
