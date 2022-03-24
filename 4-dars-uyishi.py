#%% 6-misol
lst=list(input().split())
lst=[int(i) for i in lst]
print(lst)
k=0
son=list()
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        if son!=[]:
            son.append(lst[i])
            print(*son)
            son=list()
            k+=1

#%% 7-misol
son=int(input("son="))
list1=list()
while son!=0:
    list1.append(son%10)
    son//=10
list1.reverse()
xona=['million','ming','yuz']
bir={1:'bir',
     2:'ikki',
     3:'uch',
     4:'to\'rt',
     5:'besh',
     6:'olti',
     7:'yetti',
     8:'sakkiz',
     9:'to\'qqiz'}
on={ 1:'o\'n',
     2:'yigirma',
     3:'o\'ttiz',
     4:'qirq',
     5:'ellik',
     6:'oltmish',
     7:'yetmish',
     8:'sakson',
     9:'to\'qson'}
for i in range(len(list1)-1,-1,-1):
    if i==2:    
        if list1[0]!=0:
            print(bir[list1[0]],"yuz",end=' ')
        if list1[1]!=0:
            print(on[list1[1]],end=' ')
        if list1[2]!=0:
            print(bir[list1[2]])
        elif i==1:
            if list1[0]!=0:
                print(on[list1[0]],end=' ')
            if list1[1]!=0:
                print(bir[list1[1]])
        else:
            print(bir[list1[0]])

            









