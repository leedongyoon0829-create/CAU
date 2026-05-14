import random
n=random.randint(1,100)
print('Guess your number between 1 and 100')
p=int(input('Enter your guess: '))
t=0
while p!=n:
    if p<n:
        print('Too low!')
        t+=1
        p=int(input('Enter your guess: '))
    elif p>n:
        print('Too high')
        t+=1
        p=int(input('Enter your guess: '))
   
t+=1
print(f'Congratulations! Attempts={t}')

