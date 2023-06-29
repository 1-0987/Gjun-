string_chinese= "這是一個字串"
string_chinese= "這不是一個字串吧" #先做上面再做下面，會蓋掉上面結果
print(string_chinese)
number_1 = 10
number_2 = 5
print(number_1 + number_2)
# _x = "x"
# _y = "y"
# 以上 string_chinese, number_1, _x只要符合命名邏輯，都可以改 註(ctrl+? = 快速加上#)
print(number_1, "+", number_2, "=", number_1 + number_2)
print(number_1, "-", number_2, "=", number_1 - number_2)
print(number_1, "*", number_2, "=", number_1 * number_2)
print(number_1, "/", number_2, "=", number_1 / number_2)
print(number_1, "//", number_2, "=", number_1 // number_2) # 整除
print(number_1, "%", number_2, "=", number_1 % number_2) # 餘數

import math # 使用math底下的sqrt(方根), log (非簡單算數的計算)
number_3 = 2.643
print(number_3, "的Abs(絕對值):", abs(number_3))
print(number_1, number_2, number_3, "的最大值:", max(number_1, number_2, number_3))
print(number_1, number_2, number_3, "的最小值:", min(number_1, number_2, number_3))
print(number_3, "的四捨五入是:", round(number_3))
print(number_3, "的方根是:", math.sqrt(number_3))
print(number_3, "取自然對數是:", math.log(number_3))
print(number_3, "取對數是:", math.log10(number_3))
print(number_3, "的五次方是:", pow(number_3, 5))
print(number_3, "的五次方是:", number_3 ** 5)
# 如果是負數 看以下轉換 (abs)
number_3 = -2.643
print(number_3, "的Abs(絕對值):", abs(number_3))
print(number_1, number_2, number_3, "的最大值:", max(number_1, number_2, number_3))
print(number_1, number_2, number_3, "的最小值:", min(number_1, number_2, number_3))
print(number_3, "的四捨五入是:", round(number_3))
print(number_3, "絕對值的方根是:", math.sqrt(abs(number_3)))
print(number_3, "絕對值取自然對數是:", math.log(abs(number_3)))
print(number_3, "絕對值取對數是:", math.log10(abs(number_3)))
print(number_3, "的五次方是:", pow(number_3, 5))
print(number_3, "的五次方是:", number_3 ** 5)