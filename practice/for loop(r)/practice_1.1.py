list_a = ['a', 'b', 'c', 'd', 'e']
for letter in list_a:
    print("Letter:", letter)
    for letter_upper in list_a:
        print("Letter upper", letter_upper.upper())
    print(".................") #print在不同位置有不同解答! 因為關乎做完與不做完該for才print出間隔一行