import numpy as np
x = np.random.randint(1, 10)
y = np.random.randint(1, 10)

statement = (x > y) #True則上, False則下

if statement:  #或者可改寫 if x > y (上面statement = (x>y) 可整行拿掉)
    print("x is bigger than y")
else:
    print("x is equal or smaller than y")

print(f"x:{x}, y:{y}")