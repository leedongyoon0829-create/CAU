list=[]
while True:
    n=input("숫자를 입력하시오(종료는 q): ")
    if n=="q":
        break;
    list.append(int(n))

print(f"숫자들의 합계:{sum(list)}")
print(f"숫자들의 평균:{sum(list)/len(list)}")
print(f"숫자들의 최댓값:{max(list)}")
print(f"숫자들의 최솟값:{min(list)}")
