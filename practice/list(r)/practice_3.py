#等差數列
a0 = 1
d = 6

a1 = a0 + 6
a2 = a1 + 6
a3 = a2 + 6
a4 = a3 + 6
a5 = a4 + 6

list_a = [a0, a1, a2, a3, a4]
print("list_a:", list_a, "Sum is:", sum(list_a), "Max is:", max(list_a))

sum_ad = 5 * (2 * a0 + (5 - 1) * d) / 2
print("Sum_ad is", sum_ad)