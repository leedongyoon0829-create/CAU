list=[]
num1=int(input("첫번째 정수를 입력하세요.: "))
num2=int(input("두번째 정수를 입력하세요.: "))
num3=int(input("세번째 정수를 입력하세요.: "))
list.append(num1)
list.append(num2)
list.append(num3)
list.sort()
print(f"중앙값은 {list[1]} 입니다.")
