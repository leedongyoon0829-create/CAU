n=0
list=[]
while n >= 0:
    n=int(input('Enter a score: '))
    if n>=0:
        list.append(n)
print('maximum:',max(list))
print('minimum:',min(list))
print('average:',sum(list)/len(list))
