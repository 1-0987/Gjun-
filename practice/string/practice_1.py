string_1 = '12345'
print(string_1 + "abcde")
print(f"{string_1}abcde") #f為特別字串，可以加上{} <- 變數

sound_cat = "Meow"
print(sound_cat)
print("Sound of cat is ", sound_cat, ".")
print(f"Sound of cat is {sound_cat}.")

people_name = "Leon"
print(f"{people_name}的小寫{people_name.lower()}, 再轉大寫{people_name.upper()}")
print(f"{people_name}的小寫{people_name.lower()}, 首字再轉大寫{people_name.capitalize()}")
print(people_name)