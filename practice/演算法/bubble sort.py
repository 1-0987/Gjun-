import numpy as np
n = 6
# bubbles = np.random.randint(1, 10, n)
# print(list(bubbles))
# print(sorted(bubbles))
bubbles = np.random.choice(10, n, replace=False) #表示不重複
print(list(bubbles))
# print(sorted(bubbles))

#r0=需要比到index5, r1: idx4, r2:index3 ; r + idx <=5 ;  idx <= 5-r => idx <= (6-1) -r => idx<= n-1 -r
for round, _ in enumerate(bubbles):
    for index, _ in enumerate(bubbles):
        if index < n - round - 1: #5-r
            # print("index:", index)
            print(f"Round:{round}, i:{bubbles[index]}, j:{bubbles[index + 1]}")
            print(f"Bubbles before: {bubbles}")
            if bubbles[index] > bubbles[index + 1]:
                temp = bubbles[index + 1]
                bubbles[index + 1] = bubbles[index]
                bubbles[index] = temp
            print(f"Bubbles after: {bubbles}")

