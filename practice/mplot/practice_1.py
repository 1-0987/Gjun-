# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

from matplotlib import pyplot as plt
#1
# list_y = [2, 4, 6, 8]
# plt.plot(list_y)
# # plt.show()
# plt.savefig("./practice/mplot/plot_image/first_plot.jpg")

#2
# list_x_y= [(1,2), (2,4), (9,6), (7,10)]
# list_x_y.sort()
# print(list_x_y)
# plt.plot([x for x, y in list_x_y], [y for x, y in list_x_y], marker = 'o')
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.legend(["First line"])
# plt.title("First plot")
# plt.show()
# plt.savefig("./practice/mplot/plot_image/second_plot.jpg")
# plt.cla()

#3
# n = range(1, 30)
# plt.plot(n, n, "y--") #yellow dash
# plt.plot(n, [i*i for i in n], "rs") #red square
# plt.plot(n, [i**3 for i in n], "g^") #green triangle
# plt.legend(["n", "n*n", "n*n*n"])
# plt.show()
# plt.savefig("./plot_image/third_plot.jpg")
# plt.cla

# #3
# n = range(1, 30)
# plt.plot(n, n, marker = 'o', linestyle = '--', color = 'y') #yello dash
# plt.plot(n, [i*i for i in n], "rs", linestyle = '-') #red square dash
# plt.plot(n, [i**3 for i in n], "g^--") #green triangle dash
# plt.legend(["n", "n*n", "n*n*n"])
# plt.show()
# plt.savefig("./practice/mplot/plot_image/third_plot.jpg")
# plt.cla

#4
# n = range(1, 30)
# plt.scatter(n,n,c='y')
# plt.scatter(n,[i*2 for i in n], c="r")
# plt.scatter(n,[i**3 for i in n], c="g")
# plt.legend(["n", "n*n", "n*n*n"])
# plt.show()
# plt.savefig("./practice/mplot/plot_image/forth_plot.jpg")
# plt.cla

#5
import numpy as np
x = np.random.randint(1, 100, 20) #1~100隨機20個點
y = np.linspace(1, 100, 20) #1~100等分20個點
plt.scatter(sorted(x), y, c='y')
plt.savefig("./practice/mplot/plot_image/fifth_plot.jpg")
plt.cla

#6 直方圖
x = np.random.randint(1,100,10000)
plt.hist(x,bins=10) #級距:需要小於上面的range
plt.savefig("./practice/mplot/plot_image/sixth_plot.jpg")
#可以寫另個程式去疊加進這個圖
plt.cla()

#7 圓餅圖
x = [1,2,3,40]
plt.pie(x,explode=[0.1,0.1,0.1,0.1], labels=['1','2','3','40']) #explode:餅和餅之間的偏移
plt.savefig("./practice/mplot/plot_image/seventh_plot.jpg")
plt.cla()