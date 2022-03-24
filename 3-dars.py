#%% LIST
sonlar=[1,2,3,4,5,6,7,8,9,10]
print(*sonlar)
print(*sonlar)
print(f"listning uzunligi {len(sonlar)} ta element")
sozlar=['sardor','vali','john','smith','adam']
print(*sozlar)
print(sozlar[0][0])
list1=['hello',123,True,3.14,'salom',False,-456,123465.789]
print(*list,sep='\n')
array=list(range(1,10))
print(*array)
print(list1[2])

#%% append() and insert()
list2=[1,2,3,'foundation']
list2.append(123)
list2.append(True)
list2[4]='32'
print(list2)
list2.insert(2,False)
print(list2)

#%% pop() and remove()
list3=['salom',123,'foundation 32',3.14,False,True,0]
list3.pop()
print(list3)
n=list3.pop(0)
print(list3)
print(n)
list3.remove("foundation 32")
print(list3)

#%% index(), count(), sort()
list4=[100,True,56,3.14,False,True,-400,100,100]
print(list4.index(True))
print(f"{list4[0]} qiymati {list4.count(100)} marta takrorlangan")
# list4.clear()
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
list5=['sardor','abror','azi','zuxra','javlon','aziza','aziz']
list5.sort()
print(list5)

#%% TUPLE
t1=tuple()
print(type(t1))
t2=(1.23,True,3.1415645,'salom')
print(t2)
print(t2.count('salom'))
print(t2.index('salom'))
#t2[0]=5
print(t2)
list3=list(t2)
print(list3)
list3.reverse()
print(list3)
print(list3[::-1])
print(t2[::-1])

#%% 1-misol
a=int(input("a="))
b=int(input("b="))
sonlar_juft=[]
for juft in range(a,b):
    if juft%2==0:
        #print(juft)
        sonlar_juft.append(juft)
print(sonlar_juft)

#%% 2-misol
a=int(input("a="))
b=int(input("b="))
sonlar_toq=[]
for toq in range(a,b):
    if toq%2!=0:
        #print(toq)
        sonlar_toq.append(toq)
        sonlar_toq.sort(reverse=True)
print(sonlar_toq)

#%% 3-misol
list3=['salom',123,True,'xayr','world',3.14,'7214']
text=[]
others=[]
for i in list3:
  if type(i)==str:
    text.append(i)
  else:
    others.append(i)
text.sort(reverse=False)
others.sort(reverse=True)
print(*text)
print(*others)

#%% 4-misol
# list4=list()
# n=int(input("n ni kiriting: "))
# for i in range(n):
#     list4.append(int(input(f"{i+1}-son=")))
# print(list4)
# for i in range(0,n-1):
#     for j in range(i,n-1):
        