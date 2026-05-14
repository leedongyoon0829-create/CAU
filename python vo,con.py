s=input("문자열을 입력해주세요:")
w=s.lower()
p=0
r=0
if len (s)>0 and s.isalpha():

    for char in w:
        if char in'aeiou':
            p+=1
        else:
            r+=1

print(f"모음의 개수는 {p}입니다.")
print(f"자음의 개수는 {r}입니다.")
