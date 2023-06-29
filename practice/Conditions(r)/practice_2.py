#天氣太熱
is_hot = True #習慣將需要判斷(結果為布林值)的變數取為is開頭
is_rainy = False
is_holiday = False
is_typhoon = False
is_upset = False
is_go_to_school = True

if is_hot and is_rainy:
    print("hot and rainy")
    is_go_to_school = False
if is_holiday or is_typhoon:
    print("holiday or typhoon")
    is_go_to_school = False
if is_upset and is_rainy:
    print("upset and rainy")
    is_go_to_school = False

print(is_go_to_school)

