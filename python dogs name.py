list=[]
while True:
    n=input("강아지의 이름을 입력해주세요(종료시에는 엔터키): ")

    if n=="":
        break;
    list.append(n)
print("강아지들의 이름: \n")
for d in list:
    print(d, end=", ")
    
