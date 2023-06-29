#while迴圈
#Fibonacci num < 10000
F0 = 0
F1 = 1
list_fib = [F0, F1]
while list_fib[-1] < 10000:
    list_fib.append(list_fib[-2] + list_fib[-1])
print(list_fib)
print(len(list_fib))

for index, value in enumerate(list_fib):
    if index != 0:
        print(list_fib[index - 1]/list_fib[index])