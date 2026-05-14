s=input('문자열을 입력해주세요:')
p="aeiouAEIOU"
r=""
for letter in s:
    if letter not in p:
        r+=letter
print(r)
