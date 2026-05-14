import random
list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=random.choice(list)
n=''
k=0
while n!=a:
    n=input('Enter Your guess: ')
    if n>a:
        print('Too late!')
        k+=1
    elif n<a:
        print('Too early!')
        k+=1

k+=1
print(f'Congratulations! Attempts = {k}')
