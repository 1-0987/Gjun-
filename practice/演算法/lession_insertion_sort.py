#N個數字，由小到大排序
#共N輪
#每一輪將新拿到的牌去依序比較手上的牌(已經排序好的部分)，將新牌插入序列

import numpy as np

def insertion_sort(numbers):
    sorted_numbers = list() #排序好的部分
    for round in range(len(numbers)): #共N輪
        # print("round:", round, "sorted_numbers(before):", sorted_numbers, "numbers[round]:", numbers[round])
        if round == 0:
            sorted_numbers.append(numbers[0])
            # print("round:", round, "sorted_numbers(after):", sorted_numbers)
        else:
            for index in range(len(sorted_numbers)-1, -1, -1): #去比較要放在哪裡 #round1=>0~0 #round2=>1~0 #round3=>2~1~0 #round4=>3~2~1~0 最後面的-1 就是依序遞減
                if numbers[round] > sorted_numbers[index]:
                    # print("index:", index, "sorted_numbers[index]:", sorted_numbers[index])
                    front = sorted_numbers[:index + 1] #0~index
                    back = sorted_numbers[index + 1:] #index+1 ~ end
                    # print("front:", front, "back:", back)
                    sorted_numbers = front + [numbers[round]] + back
                    # print("round:", round, "sorted_numbers:", sorted_numbers)
                    break
                if index == 0:
                    sorted_numbers = [numbers[round]] + sorted_numbers
                    # print("index:", index, "sorted_numbers(after):", sorted_numbers)
    return sorted_numbers

if __name__ == '__main__':
    N = 5
    numbers = np.random.choice(100, N, replace=False)
    print("Before:", numbers)
    print("After:", insertion_sort(numbers))
