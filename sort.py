import time
from function import *
from random import randint

s0 =[randint(-1000, 1000) for i in range(10)]
s1 = [randint(-1000, 1000) for i in range(100)]
s2 = [randint(-1000, 1000) for i in range(1000)]
s3 = [randint(-1000, 1000) for i in range(10000)]
t0 = t1 = t2 = t3 = 0




# for i in range(1):
#     bub0 = time.time()
#     bubble(s0[::])
#     bub1 = time.time()
#     bubble(s1[::])
#     bub2 = time.time()
#     bubble(s2[::])
#     bub3 = time.time()
#     bubble(s3[::])
#     bub4 = time.time()
#     t0 += (bub1 - bub0) * 1000
#     t1 +=(bub2 - bub1) * 1000
#     t2 +=(bub3 - bub2) * 1000
#     t3 += (bub4 - bub3) * 1000
#
#
# print(t0)
# print(t1)
# print(t2)
# print(t3)
#
#
#
# for i in range(1):
#     bub0 = time.time()
#     sel_sort(s0[::])
#     bub1 = time.time()
#     sel_sort(s1[::])
#     bub2 = time.time()
#     sel_sort(s2[::])
#     bub3 = time.time()
#     sel_sort(s3[::])
#     bub4 = time.time()
#     t0 += (bub1 - bub0) * 1000
#     t1 +=(bub2 - bub1) * 1000
#     t2 +=(bub3 - bub2) * 1000
#     t3 += (bub4 - bub3) * 1000
#
# print(t0)
# print(t1)
# print(t2)
# print(t3)
#
#
#
#
#
# for i in range(1):
#     bub0 = time.time()
#     insertion_sort(s0[::])
#     bub1 = time.time()
#     insertion_sort(s1[::])
#     bub2 = time.time()
#     insertion_sort(s2[::])
#     bub3 = time.time()
#     insertion_sort(s3[::])
#     bub4 = time.time()
#     t0 += (bub1 - bub0) * 1000
#     t1 +=(bub2 - bub1) * 1000
#     t2 +=(bub3 - bub2) * 1000
#     t3 += (bub4 - bub3) * 1000
#
# print(t0)
# print(t1)
# print(t2)
# print(t3)
#
#
#
#
# for i in range(1):
#     bub0 = time.time()
#     quicksort(s0[::])
#     bub1 = time.time()
#     quicksort(s1[::])
#     bub2 = time.time()
#     quicksort(s2[::])
#     bub3 = time.time()
#     quicksort(s3[::])
#     bub4 = time.time()
#     t0 += (bub1 - bub0) * 1000
#     t1 +=(bub2 - bub1) * 1000
#     t2 +=(bub3 - bub2) * 1000
#     t3 += (bub4 - bub3) * 1000
#
# print(t0)
# print(t1)
# print(t2)
# print(t3)





for i in range(1):
    bub0 = time.time()
    merge_sort(s0[::])
    bub1 = time.time()
    merge_sort(s1[::])
    bub2 = time.time()
    merge_sort(s2[::])
    bub3 = time.time()
    merge_sort(s3[::])
    bub4 = time.time()
    t0 += (bub1 - bub0) * 1000
    t1 +=(bub2 - bub1) * 1000
    t2 +=(bub3 - bub2) * 1000
    t3 += (bub4 - bub3) * 1000

print(t0)
print(t1)
print(t2)
print(t3)