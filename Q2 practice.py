E=float(input('Enter the meal cost: '))
print('choose a tip')
print('1. 10%')
print('2. 15%')
print('3. 20%')
S=int(input('Tip opinion (1,2,3): '))
if S==1:
    T=10.0
elif S==2:
    T=15.0
elif S==3:
    T=20.0
else:
    print('It is wrong option.')

print(f'Meal cost: ${E:.2f}')
print(f'Selected tip: {T:.1f}%')
print(f'Tip amount: ${E*T/100:.2f}')
print(f'Total amount to pay: ${E+E*T/100:.2f}')
