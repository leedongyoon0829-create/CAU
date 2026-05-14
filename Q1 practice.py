print('Enter a negative number to quit.')
n=0
list=[]
while n>=0:
    n=int(input('Enter a score:'))
    if n>=0:
        list.append(n)
    else:
        break;
print(f'Maximum:{max(list)}')
print(f'Minimum:{min(list)}')
print(f'Average:{sum(list)/len(list)}')
