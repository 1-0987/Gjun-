#建立隨機數列以測試
from collections import Counter #class
import numpy as np
n = np.random.randint(1, 50000) #數字串列的長度介於1-50000
print(n)
# print(x) 生成隨機數字
major_element = np.random.randint(-1*10**9, 10**9)
part_2 = np.full(n - n//2 + 1, major_element) # n/2個，必定為major_element
part_1 = np.random.randint(-1*10**9, 10**9, n//2 - 1) #不管此n//2個內容物為何，必定不影響part_2為major element
print(major_element)
test_case = np.concatenate([part_1, part_2]) #以test_case 接收，()內資料型態為arrays
# print(len(test_case), n) #測試數字陣列長度是否等於生成測試後part_1+part_2的長度
np.random.shuffle(test_case)
print(test_case, len(test_case))




