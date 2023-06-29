#practice_1.3的comprehension版本
import numpy as np
list_n = np.random.randint(1, 1000, 30)
# list_even = list()
# list_odd = list()
# list_five = list()
# list_three_or_five = list()
#應用comprehension (以以下例子而言，雖然程式簡潔但實際運算較多)
list_even = [number for number in list_n if number % 2 == 0]
list_odd = [number for number in list_n if number % 2 != 0]
list_five = [number for number in list_n if number % 5 == 0]
list_three_or_five = [number for number in list_n if number % 3 or number % 5 == 0]
print(list_odd)
print(list_even)
print(list_five)
print(list_three_or_five)
print(len(list_n))

sorted_even_numbers = sorted([number for number in list_n if number % 2 == 0 ])
for even_number in sorted_even_numbers:
    print(even_number)