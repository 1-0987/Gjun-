# 練習追code能力
a = b = c = 50
c = 40 # 50,50,40
print(a, b, c)
c = a + b # 50,50,100
a = c + b # 150,50,100
b = a + c # 150, 250, 100
print(a, b, c)
import math
a = 10
b = math.log10(a) #(10,1)
c = math.exp(b) #(10,1,e)
d = math.log(c) #(10,1,e,1)
e = math.exp2(d) #(10,1,e,1,2)
c = int(c) #10, 1, 2, 1, 2
print(a,b,c,d,e)
