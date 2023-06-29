from collections import Counter #class
list_nums = [1, 2, 3, 4, 5, 2, 2, 4, 4, 4]

number_counter = Counter(list_nums) #從藍圖(後) 蓋出 instance 實體(前)

print(number_counter, len(list_nums))
print(number_counter.most_common()) #輸出一個list，但內容物是固定的所以資料型態是tuple
print(number_counter.most_common(0)) #括號內為參數，此函數與參數關係為取前n(參數)名 =>前0名 即沒有
print("most_common(1):", number_counter.most_common(1)) #前一名
print("most_common(2):", number_counter.most_common(2)) #前兩名
print("most_common(1)[0]:", number_counter.most_common(1)[0]) #中括號內為index索引
print("most_common(1)[0][0]:", number_counter.most_common(1)[0][0])

