a0 = 1
r = 10
#1 方法1
a1 = a0 * r
a2 = a1 * r
a3 = a2 * r
a4 = a3 * r
a5 = a4 * r
a6 = a5 * r
a7 = a6 * r
a8 = a7 * r

list_ar = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
print(sum(list_ar))

#方法2
sum_ar = a0 * (1 - pow(r, 9)) / (1 - r)
print(sum_ar)
print(int(sum_ar)) #去小數點