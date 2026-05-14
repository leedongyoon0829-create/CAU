P=float(input('Enter the drink price: '))
print('Choose a discount: ')
print('1.5%')
print('2.10%')
print('3.20%')
c=int(input('discount option (1/2/3): '))
if c==1:
    d=5.0
    print(f'Original price: {P:.2f} KRW')
    print(f'Selected discount: {d:.1f}%')
    print(f'Discount amount: {P*d/100:.2f} KRW')
    print(f'Final price: {P-P*d/100:.2f} KRW')
elif c==2:
    d=10.0
    print(f'Original price: {P:.2f} KRW')
    print(f'Selected discount: {d:.1f}%')
    print(f'Discount amount: {P*d/100:.2f} KRW')
    print(f'Final price: {P-P*d/100:.2f} KRW')
elif c==3:
    d=20.0
    print(f'Original price: {P:.2f} KRW')
    print(f'Selected discount: {d:.1f}%')
    print(f'Discount amount: {P*d/100:.2f} KRW')
    print(f'Final price: {P-P*d/100:.2f} KRW')
else:
    print('Wrong choice.')
