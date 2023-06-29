a = "1010" #10 (以2進位來看)
b = "1011" #11 (以2進位來看)
# print(a + b) #直接字串相連
# print(int(a), int(b), int(a) + int(b)) #字串改為數字 #一般預設即為10進位
# print(int(a, 2), int(b, 2), int(a, 2) + int(b, 2)) #以2進位看
c = int(a, 2) + int(b, 2) #21 => 下題為改成2進位應為...

binary_string = ""

while c > 1:
    remainder = c % 2 #餘數
    c = c//2 #c改為可整除2的商
    binary_string = str(remainder) + binary_string
    print(f"c = {c}, r = {remainder}, bs = {binary_string}")
# 除一次2的餘數為2進位的最末位，除兩次2的餘數(等於除一次2的商拿去再除一次2的餘數)為2進位末2位的值,,,
binary_string = str(c) + binary_string
print("binary string:", binary_string)
