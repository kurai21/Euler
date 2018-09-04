# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



print(50 + 2*25 + 4*12 + 8*6 + 16*3)

A = range(1, 101)
import math
import time

t1 = time.time()


def issimple(a):
    if a == 1:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    else:
        return True


def find_all_prime(a):
    b = []
    for i in range(1, a):
        if issimple(i):
            b.append(i)
    return b


set_prime = set()
for i in A:
    for j in find_all_prime(i):
        set_prime.add(j)
set_prime.remove(1)
print(set_prime)

dict_prime = dict()
for i in set_prime:
    dict_prime.setdefault(str(i), 0)
print(dict_prime)

for i in A:
    for j in set_prime:
        if i == j:
            dict_prime[str(j)] = 1
            break
        b = 0
        c = i
        while True:
            if c % j == 0 and float(c) / float(j) == float(c / j):
                c = c / j
                b += 1
            else:
                break
        if dict_prime[str(j)] < b:
            dict_prime[str(j)] = b

print(dict_prime)

final = 1
for i in set_prime:
    final *= i ** dict_prime[str(i)]
print(final)


t2 = time.time() - t1
print(t2)


#
# t1 = time.time()
# i = 0
#
# while i < math.factorial(20):
#     i += 20
# t2 = time.time() - t1
# print(t2)
