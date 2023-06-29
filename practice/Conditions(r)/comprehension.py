import numpy as np
x = np.random.randint(1, 10)
y = np.random.randint(1, 10)

# if x > y:
#     print("x is bigger than y")
# else:
#     if x==y:
#         print("x is equal to y")
#     else:
#         print("x is smaller than y")

if x > y:
    print("x is bigger than y")
elif x==y: #else-if
    print("x is equal to y")
else:
    print("x is smaller than y")

print(f"x:{x}, y:{y}")

#comprehension #如果只有一個條件，可以寫成以下，若多層條件，只能寫以上
result = "x is bigger than y" if x > y else "x is smaller than or equal to y"
print(result)