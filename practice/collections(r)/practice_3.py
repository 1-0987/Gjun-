from collections import Counter

def find_max_frequency(numbers):
    # 使用Counter計算每個數字的頻率
    frequency_counter = Counter(numbers)

    # 找出頻率最高的數字
    max_frequency = max(frequency_counter.values())

    # 找出所有頻率等於最高頻率的數字
    most_frequent_numbers = [number for number, frequency in frequency_counter.items() if frequency == max_frequency]

    return most_frequent_numbers

# 測試程式碼
number_list = [1, 2, 3, 4, 5, 2, 2, 4, 4, 4]
most_frequent = find_max_frequency(number_list)
print("Most frequent numbers:", most_frequent)