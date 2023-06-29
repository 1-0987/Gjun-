from 費撥那切數列 import find_fibonacci
from gcd_function import find_gcd
import math
import numpy as np

print("hello")

#抄下面的去執行
# n = 2 #兩個最大公因數
# numbers = np.random.choice(1000, n, replace=False)
# print("Numbers:", numbers, math.gcd(*numbers))
# result = find_gcd(numbers)
# print(result)

fibs = find_fibonacci(10000)
print("find_fibonacci(10000):", fibs)