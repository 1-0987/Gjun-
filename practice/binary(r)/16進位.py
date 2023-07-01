a = "1010"
b = "1011"
c = int(a, 16) + int(b, 16)

hexa_string = ""

while c > 1:
    remainder = c % 16
    c = c//16
    hexa_string = str(remainder) + hexa_string
    print(f"c = {c}, r = {remainder}, bs = {hexa_string}")
binary_string = str(c) + hexa_string
print("hexa_string:!!!", hexa_string)

