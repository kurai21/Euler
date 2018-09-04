# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math
sq_sum = 0
sum_sqt = 0

for i in range(1, 101):
    sq_sum = sq_sum + i
    sum_sqt = sum_sqt + pow(i, 2)

print(pow(sq_sum, 2) - sum_sqt)
