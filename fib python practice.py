n=int(input('정수를 입력하시오: '))
def feb(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>=2:
        return feb(n-1)+feb(n-2)

print(f'{n} 번째 피보나치 수는',feb(n))
