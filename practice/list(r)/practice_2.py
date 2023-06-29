list_3 = [1, 2, 3, 4, 5, 6, 7]
x = list_3[0] #1(由0開始)
y = list_3[5] #6
z = list_3[-1] #7 (負數代表由後面  往前算)
w = list_3[1:3] #[2,3] (表示由第一位(其實是2!)算到不包括3)
v = list_3[1:-1] #[2,3,4,5,6]
print(x, y, z, w, v)

list_3[-1] = [55, 66] #[1,2,3,4,5,6, [55,66]]
list_3[1:3] =[10, 11] #[1, 10, 11, 4, 5, 6, [55, 66]]
print(list_3)

# append: 元素相加
# extend: 序列相加
list_4 = ["A", "B", "C"]
list_4.append("D") #["A", "B", "C", "D"]
print(list_4)
list_4 = ["A", "B", "C"]
list_4.extend(["E", "F"]) #["A", "B", "C", "D", "E", "F"]
print(list_4)
list_4.append(["G", "H"]) #["A", "B", "C", "D", "E", "F", ["G", "H"]]
print(list_4)
list_4.extend("X")
print(list_4) #not wrong anymore

# pop, remove pop去除最後一項; remove為去除選定的第一項
pop_1 = list_4.pop()
print(pop_1) #被pop掉的東西
print("pop!", pop_1, ", list:", list_4)
list_4.remove("E")
print("remove!", list_4)

# sort
list_for_sort = [5, 6, 8, 1, 9, 8, 9]
list_for_sort.sort()
print("sorted", list_for_sort)
list_for_sort.sort(reverse = True)
print("sort(reversed):", list_for_sort)
list_for_sorted = [5, 6, 8, 9, 9, 1, 3, 4]
print("Sorted:", sorted(list_for_sorted)) #list變數+sort() = sorted(變數list)
print("Original:", list_for_sorted)