#%% 1-misol
dic={}
lst=[]
n=int(input("nechta element kiritasiz: "))
while len(dic)<n:
    key=int(input("key="))
    value=int(input("value="))
    dic[key]=(value)
sorted_values = sorted(dic.values())
sorted_dict = {}
for i in sorted_values:
    for k in dic.keys():
        if dic[k] == i:
            sorted_dict[k] = dic[k]
            break
print(sorted_dict)
print(max(sorted_dict),end=" ")
later=sorted_dict.pop(max(sorted_dict))
print(max(sorted_dict))
#%%
string1='Python'
string2=string1[2:]+string1[:2]
print(string1 in 2*string2)

#RESULT:True

#%%
a=[[0,1,2],[7,8,9],[4,5,6]]
# print([x for y in a for x in y])
list=[]
for y in a:
    for x in y:
        list.append(x)
print(list) 

#RESULT:[0, 1, 2, 7, 8, 9, 4, 5, 6]

#%%
tuple=(1,2,3)
values=tuple,4,5
print(values)

#RESULT:((1, 2, 3), 4, 5)

#%%
list=[1,2,3,4,5,6]
for i in range(1,6):
    list[i-1]=list[i]
for j in range(0,6):
    print(list[j],end=" ")
    
#RESULT:2 3 4 5 6 6 

#%% 
tuple=(1,2,3,4,1,2,3,4,5)
print(tuple.__len__())

#RESULT:9

#%%
string='python'
for i in string:
    print(i[len(i)-2],end=" ")
    
#RESULT:p y t h o n 

#%%
x,y,z=7,2,5
print(pow(x,y,z))

#RESULT:4

#%%
x={1,3,8}
y={5,2,3}
z=x.intersection(y)
print(z)

#RESULT:{3}

#%%
list=[1,0,2]
a,b,c=list[::-1]
print(list[b])

#RESULT:1

#%%
list=[10,20,30]
i=list[1]
for i in list:
    i+=1
    print(i,end=" ")
    
#RESULT:11 21 31

#%%
string='abcd'
for s in range(len(string)):
    print(s,end=" ")
    
#RESULT:0 1 2 3

#%%
a=[]
b=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
for i in range(4):
    a.append([row[i] for row in b])
print(a)

#RESULT:[[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]

#%%
for i in [1,2,3,4][::-1]:
    print(i,end=" ")

#RESULT:4 3 2 1

#%%
x=.2,3.,.4
print(x[1]+x[2])

#RESULT:3.4

#%%
list=[10,20,30]
list.extend(list)
print(list)

#RESULT:[10, 20, 30, 10, 20, 30]

#%%
x={7>5,2>8,0}
print(all(x))

#RESULT:False

#%%
list=[0,1,2,3]
for list[-1] in list:
    print(list[-1],end=" ")
    
#RESULT:0 1 2 2

#%%
x,y=10,15
x=x^y
y=x^y
x=x^y
print(x,y)

#RESULT:15 10

#%%
string='interview'
new_str=string.replace('e','-',1)
print(new_str)

#RESULT:int-rview

#%%
a=[[0,1,2],[7,8,9],[4,5,6]]
print([x for y in a for x in y])

#RESULT:[0, 1, 2, 7, 8, 9, 4, 5, 6]

#%%
a,b='12'
b,c='34'
print(a,b,c)

#RESULT:1 3 4

#%%
tuple=(1,2,3)
values=tuple,4,5
print(values)

#RESULT:((1, 2, 3), 4, 5)

#%%
x,y=15,2
sum_=(x>>y)+(x<<y)
print(sum_)

#RESULT:63

#%%
x=['1','2','3']
y=x[1]+x[2]
print(y)

#RESULT:23

#%%
numbers=[5,12,25,31,43,23,45,24,10,50]
for x in numbers:
    if x%5==0 and x%10==0:
        print(x,end=" ")

#RESULT:10 50

#%%
numbers=[5,12,25,31,43,23,45,24,10,50]
for x in numbers:
    if x%5==0 or x%10==0:
        print(x,end=" ")

#RESULT:5 25 45 10 50 

#%%
for i in range(20):
    if i<18 and i>8:
        if i%2==0:
            print(i,end=" ")
            
#RESULT:10 12 14 16 

#%%
dict={1:4,2:8,5:16,8:32}
print(list(dict.values())[2])

#RESULT:16

#%%
list=[5,4,3,2]
list.insert(1,2)
print(list)

#RESULT:[5, 2, 4, 3, 2]

#%%
string='python'
x='y'
while x in string:
    print(x,end=" ")
    
#RESULT:y y y y y y ...

#%%
x=(i for i in range(3))
for i in x:
    print(i,end=" ")
for i in x:
    print(i)
    
#RESULT:0 1 2

#%%
tuple1=(1,2,3)
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)

#RESULT:(1, 2, 3, 1, 2, 3)

#%%
list=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]
for i in range(0,4):
    print(list[i][1],end=" ")
    
#RESULT:2 6 10 14 

#%%
fib=[0,1]
[fib.append(fib[-2]+fib[-1]) for i in range(8)]
print(fib)

#RESULT:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#%%
list1=[1,2]
list2=list1
list1[0]=3
print(list2)

#RESULT:[3, 2]

#%%
dict={'x':10,'y':20}
print('y' in dict)
#RESULT:True
dict={'x':10,'y':20}
print('y' in dict)
#RESULT:False

#%%
string='xyyzxyzxzxyy'
count=string.count('yy',3)#.count(x='yy',start=2,end)
print(count)
#RESLUT:1
string='xyyzxyzxzxyy'
count=string.count('yy')#.count(x='yy',start,end)
print(count)
#RESLUT:2

#%%
dict={}
list1=[1,2,3]
list2=[4,5,6]
print(dict.fromkeys(list1,list2))

#RESULT:{1: [4, 5, 6], 2: [4, 5, 6], 3: [4, 5, 6]}

#%%
string='python'
print(string.find('ph'))

#RESULT:-1

#%%
x={1,2,3,4}
y={3,4,5}
print(x.difference(y))

#RESULT:{1, 2}

#%%
elements=[5,2,4,5,2,5,4]
most_repeated=max(elements,key=elements.count)
print(most_repeated)

#RESULT:5

#%%
x={'a':5,'b':10}
y=dict(zip(x.values(),x.keys()))
print(y)

#RESULT:{5: 'a', 10: 'b'}

#%%
dict={1:2,3:4,5:6}
dict.pop(3,5)
print(dict)

#RESULT:{1: 2, 5: 6}

#%%
string='python___developers'
new_str=""
for s in string:
    if s=="_":
        continue
    new_str+=s
print(new_str)

#RESULT:pythondevelopers

#%%
list=[4,3.1,'2']
list.sort()
print(list)

#RESULT:Error

#%%
x={}
x[2]=5
x[1]=[2,3,4]
print(x[1][1])

#RESULT:3

#%%
s=0
for i in range(10,1,-1):
    s-=i
print(s)

#RESULT:-54

#%%
a={5,4}
b={1,2,3,4}
print(a<b)

#RESULT:False

#%%
tuple=('python')*3
print(tuple)

#RESULT:pythonpythonpython

#%%
a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)

#RESULT:[1, 3, 6, 10]

#%%
for i in range(10):
    if i==5:
        break
    else:
        print(i,end=" ")
        
#RESULT:0 1 2 3 4 

#%%
list=[[]]*3
list[1].append(5)
print(list)

#RESULT:[[5], [5], [5]]

#%%
s='hello'
l=list((x,len(x)) for x in s)
print(l)

#RESULT:[('h', 1), ('e', 1), ('l', 1), ('l', 1), ('o', 1)]

#%%
dict={'A':'Hello','B':'World'}
print('{A}{B}'.format(**dict))

#RESULT:HelloWorld

#%%
x=['P','y','t','h','o','n']
for i in enumerate(x):
    print(i,end=" ")

#RESULT:(0, 'P') (1, 'y') (2, 't') (3, 'h') (4, 'o') (5, 'n') 

#%%

a={1,2,3,4}
b={3,4,5}
print(a.union(b))

#RESULT:{1, 2, 3, 4, 5}

#%%










































































































