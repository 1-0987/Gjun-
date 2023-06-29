#refactor 整理
is_hot = True
is_rainy = False
is_holiday = False
is_typhoon = False
is_upset = False
is_go_to_school = True

if ((is_hot or is_upset) and is_rainy) or \
    (is_holiday or is_typhoon):
    is_go_to_school = False

print(is_go_to_school)
