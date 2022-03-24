#%% 1-misol
list1=[1,2,3]   
list2=[11, 22, 33]
list3=[]
if(len(list1)==len(list2)):
    list3 = [i for j in zip(list1, list2) for i in j]
    print(list3)
elif(len(list1)>len(list2)):
    list3 = [i for j in zip(list1, list2) for i in j]
    list3.append(list1[len(list2):len(list1)])
    print(list3)
elif(len(list1)<len(list2)):
    list3 = [i for j in zip(list1, list2) for i in j]
    list3.append(list2[len(list1):len(list2)])
    print(list3)
#%% 2-misol
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=set(a)
d=c.intersection(b)
e=list(d)
print(e)

#%% 3-misol
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)
c.sort(reverse=False)
print(c)























































































































































