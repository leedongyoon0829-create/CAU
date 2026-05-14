import math
def circle(r):
    a=math.pi*r*r
    b=math.pi*2*r
    return(a,b)
r=float(input("원의 반지름을 입력하시오: "))
(p,q)=circle(r)
print(f"원의 넒이는 {str(p)}이고 원의 둘레는 {str(q)}이다.")
