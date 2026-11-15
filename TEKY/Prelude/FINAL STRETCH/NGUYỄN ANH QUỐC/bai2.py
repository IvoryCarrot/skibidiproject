import random
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listabc = list(abc)
number = "0123456789"
listnumber = list(number)
a = 0
randomness = 0
password = ""
criteria = False
while a != 6:
    randomness = random.randint(0,1)
    if randomness == 0:
        password += random.choice(listabc)
    elif randomness == 1:
        password += random.choice(listnumber)
    if password[a].isdigit:
        criteria = True
    a += 1
print(f"Mã xác nhận: {password}\nCó chứa chữ số: {criteria}")