from collections import Counter
import numpy as np
n = np.random.randint(1, 50000)
major_element = np.random.randint(-1*10**9, 10**9)
part_2 = np.full(n - n//2 + 1, major_element)
part_1 = np.random.randint(-1*10**9, 10**9, n//2 - 1)
print("major_element: ", major_element)
test_case = np.concatenate([part_1, part_2])
list_nums = test_case
number_counter = Counter(list_nums)  #9-10為計算list內的公式
# print(number_counter, len(list_nums))
print("major element:", number_counter.most_common(1)[0][0])
print("major element數目:", number_counter.most_common(1)[0][1])
print(len(list_nums))