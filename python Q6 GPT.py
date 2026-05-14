c=0
list=[]
while c!=9:
    print('----------------------')
    print('1. Show Fruit List')
    print('2. Add Fruit')
    print('3. Delete Fruit')
    print('4. Change Name')
    print('9. Exit')

    c=int(input('Select a menu option: '))
    if c==1:
        print('Fruit List: ',list)
    elif c==2:
        k=input('What fruit do you want to add?: ')
        list.append(k)
    elif c==3:
        t=input('What fruit do you want to delete?: ')
        if t in list:
            list.remove(t)
        else:
            print('The fruit you wrote is not in the list.')
    elif c==4:
         r=input('What fruit do you want to change?: ')
         if r in list:
             idx=list.index(r)
             n=input('Write the fruit you want to replace with ')
             list[idx]=n
         else:
             print('The fruit you wrote is not in the list.')
    elif c==9:
        break
    else:
        print('Wrong option.')

print('Thank you!')
    
