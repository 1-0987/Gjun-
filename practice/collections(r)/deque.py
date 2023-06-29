#擴充資料型態(非基本資料型態)
#deque可視為可以兩頭運算的list
from collections import deque
from collections import Counter
deque_1 = deque([1, 2, 3])
deque_1.append(4)
deque_1.extend([5, 6, 7])
print(deque_1)
# list 加入東西到左邊，要用此形式 : list_a = ["a"] + ["b", "c", "d"]
#但 deque 可以使用加入到左側的程式
deque_1.appendleft(0)
deque_1.extendleft([10, 9, 8]) #會變成反過來貼
print(deque_1)
deque_1 = [11, 12, 13] + list(deque_1) #要相加(若要正貼非反貼)要先變回list
print(deque_1)
deque_2 = deque(["a", "b", "c", "d", "e"], maxlen=7) #最大長度為7
deque_2.rotate(1) #轉一次(將e提到前面)
print(deque_2)
deque_2.rotate(2) #轉2次(新的eabcd再轉2次)
print(deque_2)
deque_2.extendleft(["f", "g", "h"]) #以新的為主，會把舊的擠掉
print(deque_2)

# Counter
counter_1 = Counter([5, 5, 6, 7, 8, 9, 1, 3])
print(counter_1)
print(counter_1[5])

# application應用題
# counter



