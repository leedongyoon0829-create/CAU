import random
chars='abcdefghijklmnopqrstuvwxyz0123456789'
for _ in range (3):
    password=''
    for _ in range(6):
        password+=random.choice(chars)
    print(password)
