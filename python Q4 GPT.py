import random
list='abcdefghijklmnopqrstuvwxyz0123456789'
for _ in range(5):
    p=''
    for _ in range(8):
        p+=random.choice(list)

    print(p)
        
