list=[]
n=0
g1=int(input("성적을 입력하시오: "))
list.append(g1)
g2=int(input("성적을 입력하시오: "))
list.append(g2)
g3=int(input("성적을 입력하시오: "))
list.append(g3)
g4=int(input("성적을 입력하시오: "))
list.append(g4)
g5=int(input("성적을 입력하시오: "))
list.append(g5)
print(f"성적 평균은 {(list[0]+list[1]+list[2]+list[3]+list[4])/5} 입니다.")
if g1>=80:
    n+=1
if g2>=80:
    n+=1
if g3>=80:
    n+=1
if g4>=80:
    n+=1
if g5>=80:
    n+=1

print(f"80점 이상을 받은 학생은 {n} 명입니다.")
