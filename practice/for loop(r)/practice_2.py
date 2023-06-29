list_a = range(1, 101)
# list_a = range(101)
# print(list_a) #generator:有需要才會印出來
# print(list(list_a)) #強迫印出來XD
print(list(list_a))

list_square = list()
for x in list_a:
    list_square.append(x ** 2)
print(list_square, len(list_square))
#轉comprehension
list_square = [x ** 2 for x in list_a]
print(list_square, len(list_square))