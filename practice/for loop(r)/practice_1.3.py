import numpy as np
list_n = np.random.randint(1, 1000, 30)

list_even = list()
list_odd = list()
list_five = list()
list_three_or_five = list()

for number in list_n:
    if number % 2 == 0: #even
        list_even.append(number) #偶數隊+1 !
    else:
        list_odd.append(number) #奇數隊+1 !
    if number % 5 == 0:
        list_five.append(number)
        list_three_or_five.append(number)
    elif number % 3 == 0:
        list_three_or_five.append(number)
print(list_odd)
print(list_even)
print(list_five)
print(list_three_or_five)
print(len(list_n))
