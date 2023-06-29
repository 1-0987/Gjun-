list_a = ['a', 'b', 'c', 'd', 'e']

print(list_a)
# #還不會for loop前想要印出內容物的方法
# print(list_a)
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[3])
# print(list_a[4])

#replace with for-loop

for letter in list_a:
    print("Letter:", letter)
    for letter_upper in list_a:
        print("Letter upper", letter_upper.upper())
