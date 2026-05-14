n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
s=input('Enter an operator(+,-,*,/): ')
if s=='+':
    print(f'Result: {n1+n2}')
elif s=='-':
    print(f'Result: {n1-n2}')
elif s=='*':
    print(f'Result: {n1*n2}')
elif s=='/':
    print(f'Result: {n1/n2}')
else:
    print('That is wrong input.')
