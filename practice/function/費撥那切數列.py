def find_fibonacci(constraint):
    F0 = 0
    F1 = 1
    list_fib = [F0, F1]
    while list_fib[-1] < constraint:
        list_fib.append(list_fib[-2] + list_fib[-1])
    return list_fib[:-1] #加至倒數第二項(因為最後一項會大於10000)

if __name__ == '__main__':
        fibs = find_fibonacci(10000)
        print("find_fibonacci(10000):", fibs)
        fibs = find_fibonacci(20000)
        print("find_fibonacci(20000):", fibs)
        fibs = find_fibonacci(30000)
        print("find_fibonacci(30000):", fibs)
