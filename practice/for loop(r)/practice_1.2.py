list_a = ['a', 'b', 'c', 'd', 'e']
for index, letter in enumerate(list_a):
    print(index, ":", letter)
    index = index + 1 #不會影響最初list_a的index(次序)
    print(index, "+", letter * index)