n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
o=input('Enter an operator (>,<,==): ')
if o=='>':
    print(n1>n2)
elif o=='<':
    print(n1<n2)
elif o=='==':
    print(n1==n2)
else:
    print('Wrong operator.')
