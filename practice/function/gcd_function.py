import math
import numpy as np

def find_divisor_of_min(numbers):
    min_num = min(numbers)
    divisors_of_min = list()
    for n in range(1, min_num + 1):
        if min_num % n == 0:
            divisors_of_min.append(n)
    return divisors_of_min

def find_gcd(numbers):
    divisors = find_divisor_of_min(numbers)
    list_of_common_divisors = list()
    for divisor in divisors:
        is_common_divisor = True
        for number in numbers:
            if number % divisor == 0:
                continue
            else:
                is_common_divisor = False
                break
        if is_common_divisor == True:
            list_of_common_divisors.append(divisor)
    return max(list_of_common_divisors)

if __name__ == '__main__':
    n = 2 #兩個最大公因數
    for _n in range(3): #做三次
        numbers = np.random.choice(1000, n, replace=False)
        print("Numbers:", numbers, math.gcd(*numbers))
        result = find_gcd(numbers)
        print(result)