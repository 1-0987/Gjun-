list_1 = list() #空列
list_2 = []

string_for_list = "I want to play a game".replace(" ", "**")
print(string_for_list)
list_from_string = string_for_list.split("**")
print(list_from_string)
list_from_string_2 = "Eat an apple a day, keep doctor away".split(" ")
print(list_from_string_2)
string_for_list_2 = string_for_list.replace("**", "%%")
print(string_for_list_2)

