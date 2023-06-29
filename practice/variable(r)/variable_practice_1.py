# 練習追code能力
a = b = c = 50
c = 40 # 50,50,40
print(a, b, c)
c = a + b # 50,50,100
a = c + b # 150,50,100
b = a + c # 150, 250, 100
print(a, b, c)