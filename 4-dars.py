#%% SET
s1=set() #bo'sh set e'lon qilish
s1={1,1,3,1,531,1,15,14,311,651,63,1}
print(s1,type(s1))
s1={1,'salom',3,False,5}
s2={0,1,2,3,4,5}
# s2.add(int(input("text:")))
# print(s2)
# #s2.clear()
# print(s2)
print(s1.difference(s2)) #s1 ning s2 dan farqini chiqaradi
print(s2.difference(s1)) #s2 ning s1 dan farqini chiqaradi
print(s2.intersection(s1)) #s1 da ham s2 da ham borlarini chiqaradi
print(s2.union(s1))
print(sum(s2),max(s2),min(s2))
for i in range(int(input("nechta:"))):
    s1.pop()
s1.remove('salom')
# s1.update((1,2,3,4,5,6,7,8,9))
s1.update(s2)
print(s1)

#%% DICTIONARY
dict1=dict() #bo'sh dictionary
dict1={2:'salom','xayr':'alvido',False:True,True:False}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict2={1:[1,2,3,4,5,6,7,8,9],'salom':('kuku','qwerty')}
print(*dict2.values())
dict3={True:2,1:False,100:'yuuuuuuuz'}
print(dict3)
dict4={100:'yuz',200:'yuz'}
dict4[500]=1000
print(dict4)
dict3.update(dict4)
print(dict3)
dict4.pop(100)
print(dict4)
dict2.pop(1)
print(dict2)
dict4.popitem()
print(dict4)
                 
#%% 1-misol
lst=[(10,20,30),(40,50,60),(70,80,90)]
tpl=()
print(type(lst),type(lst[0]))
tpl[lst[0],lst[1],lst[2]]
print(tpl)

#%% 4-misol
text=input("text:")
lssst=[]
print(type(text))
lssst.append(text)
tppl=tuple(*lssst)
print(tppl)
print(type(tppl))