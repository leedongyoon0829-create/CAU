def c(t):
    w=t.split()
    uw=set(w)
    return len(uw)
t=input('문자열을 입력하세요:')
print(f'중복되지 않은 단어의 개수:{c(t)}')
