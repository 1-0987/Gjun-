import math
import numpy as np
n = 3
numbers = np.random.choice(1000, 3, replace=False)
print(numbers)
#print(numbers, math.gcd(*numbers)) 正解驗算

# 思路: (1)找最小數 (2)找最小數的因數 (3)確認是否為公因數 (4)其中最大的公因數為最大公因數

#1
min_num = min(numbers)
#2 時間複雜度:O(N)
divisors = list()
for n in range(1, min_num + 1):
    if min_num % n == 0:
        divisors.append(n)
print(min_num, "'s divisors:", divisors)


#3 時間複雜度:O(M*N), M=len(Divisor), N=len(Number)
common_divisors = list()
for divisor in divisors:
    is_common_divisor = True #假設為真
    for number in numbers:  #以下為驗證是否為真
        if number % divisor == 0:
            continue
        else:
            is_common_divisor = False
            break

    if is_common_divisor == True:
        common_divisors.append(divisor)

print("common divisors:", common_divisors)

#4
print("max common divisors:", max(common_divisors))