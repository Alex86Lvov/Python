#1 не получилось обыграть try except на return пишет, что внешняя функция
from sys import argv
a, b, c = map(int, argv[1:])
x = a * b +c
print(x)


#2
# old = [2, 3, 23, 2, 45, 14, 10, 6, 23, 12, 5, 48]
# new = [old[i + 1] for i in range(len(old) - 1) if old[i] < old[i + 1]]
# print(new)


#3
# n = [i for i in range(20, 241) if i % 21 == 0]
# print(n)


#4
# k = [2, 3, 2, 5, 3, 1, 5, 6, 34, 3, 6, 5, 7, 2, 4, 12, 5]
# r = [i for i in range(len(k)) if k.count(i) == 1]
# print(r)

#5
# from functools import reduce
# m = [i for i in range(100, 1001) if i % 2 == 0]
# mult_all = reduce(lambda x,y: x * y, m)
# print(mult_all)


#6.1
# import itertools
# for i in itertools.count(5, 4):
#     if i > 40:
#         break
#     else:
#         print(i)
#
# a = 1
# for i in itertools.cycle(["Hello", "Big", "World"]):
#     if a > 16:
#         break
#     else:
#         print(i)
#         a += 1