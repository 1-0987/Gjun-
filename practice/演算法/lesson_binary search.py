import numpy as np
from lession_insertion_sort import insertion_sort


def binary_search(numbers, target):
    start, end = 0, len(numbers) - 1
    while start <= end: #派出start, end從兩頭搜尋target，不斷根據與target的相對大小調整，直到start = end 即為target
        mid = (start + end) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print("target not found")
    return -1


if __name__ == '__main__':
    N = 5
    numbers = numbers = np.random.choice(100, N, replace=False)
    numbers = insertion_sort(numbers)
    target = np.random.choice(numbers, 1)[0]
    print(numbers, target)
    target_index = binary_search(numbers, target)
    print(numbers[target_index], target)
