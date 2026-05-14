list=[]
while True:
    print("---------------------------")
    print("1.친구 리스트 출력")
    print("2.친구 추가")
    print("3.친구 삭제")
    print("4.이름 변경")
    print("9.종료")
    n=int(input('메뉴를 선택하시오:'))
    if n==1:
        print('친구 리스트를 출력합니다.')
        print(list)
    elif n==2:
        n=input('이름을 입력하시오: ')
        list.append(n)
    elif n==3:
        print(list)
        p=input('지우고 싶은 이름을 적으시오: ')
        if p in list:
            list.remove(p)
        else:
            print('리스트에 선택하신 이름이 없습니다.')
    elif n==4:
        print(list)
        k=input('바꾸고 싶은 이름을 적으시오: ')
        if k in list:
            s=input('새로 바꿀 이름을 입력해주세요: ')
            l=list.index(k)
            list[l]=s
        else:
            print('리스트에 선택하신 이름이 없습니다.')
    elif n==9:
        print('종료되었습니다.')
        break;
    else:
        print('메뉴에 없는 숫자입니다.다시 확인 부탁드립니다.' )
        

    
