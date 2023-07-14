import numpy as np

def merge(left_array, right_array):
    result = list()
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] < right_array[0]:
            result.append(left_array.pop(0))
        else:
            result.append(right_array.pop(0))
    if len(left_array) > 0:
        result += left_array #result = result + left_array
    else:
        result += right_array
    return result

def merge_sort(numbers):
    if len(numbers) == 1: #剩下一個的狀況，已經排好了，直接完成
        return numbers
    middle_index = len(numbers) // 2
    left_array, right_array = numbers[:middle_index], numbers[middle_index:]
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)
    sorted_numbers = merge(sorted_left_array, sorted_right_array)
    return sorted_numbers

if __name__ == '__main__':
    N = 10
    numbers = np.random.choice(100, N, replace=False).tolist()
    print("Before:", numbers)
    print("After:", merge_sort(numbers))