list_height = [177, 180, 191, 164, 194]
list_name =  ["Wu", "Lin", "Xia", "Chang", "Chen"]
list_tuple = [
    (list_name[0], list_height[0]),
    (list_name[1], list_height[1]),
    (list_name[2], list_height[2]),
    (list_name[3], list_height[3]),
    (list_name[4], list_height[4]),
]
print(list_tuple)
print("Tuple(name, height): ", sorted(list_tuple)) #以name排序
print("Tuple(height, name): ", sorted(list_tuple, key = lambda x:x[1])) #由後面的變數-以height排序
sorted_1 = sorted(list_tuple, key = lambda x:x[1])
print(sorted_1)
sorted_2 = sorted(list_tuple, key = lambda x:x[1], reverse= True)
print(sorted_2)
sorted_1.sort(reverse = True) #不特別指定會由name排(前面的變數)，並顛倒
print(sorted_1)