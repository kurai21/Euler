# https://projecteuler.net/problem=4


def poli(a):
    a = str(a)
    r = a[::-1]
    return(a == r)


b = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if poli(i * j):
            b.append(i * j)
print(max(b))
