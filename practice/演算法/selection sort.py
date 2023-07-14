#N個無序數字，要把數字由小到大排序
#1.每一輪，會把最小的數字，放到對應的位置
#e.g.第一輪，把最小的數字放到第一個
#    第二輪，把次小的數字放到第二位...
# 共要做N-1輪
import numpy as np

def selection_sort(numbers):
    for round in range(len(numbers)): #第0~4輪
    # print("Round:", round, "postulated mini:", original_list[round])
    #預設每一輪的最小值是最前面一位
        for index, element in enumerate(numbers):
            round_minimum = numbers[round]
            round_minimum_index = round
            #找最小值
            for index in range(round, len(numbers)):
                if numbers[index] < round_minimum:
                    round_minimum = numbers[index]
                    round_minimum_index = index
            #交換
            if round != round_minimum_index:
                numbers[round], numbers[round_minimum_index] = numbers[round_minimum_index], numbers[round]
        # print("real mini", numbers[round_minimum_index], "staged result:", numbers)
    return numbers

if __name__ == '__main__':
    N = 5
    numbers = np.random.choice(100, N, replace=False)
    print("Before:", numbers)
    # original_list = numbers
    print("After:", selection_sort(numbers))