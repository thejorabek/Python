import colorama as c
matn=input("Matnni kiriting: ")
for i in matn:
    if i in 'AaBbCcDdEeFfGgHh':
        print(c.Fore.RED,i,end='')
    elif i in 'IiJjKkLlMmNnOoPp':
        print(c.Fore.YELLOW,i,end='')
    elif i in 'QqRrSsTtUuVvWwXxYyZz':
        print(c.Fore.GREEN,i,end='')
print(c.Style.RESET_ALL)

#%%
n=int()
son=input("son: ")
lst=str()
for i in son:
    lst+=str((int(i)+7)%10)
print(lst)

#%%
import random as rand
from random import choice
list1 = list()
list2 = list()
for i in range (999):
    i=rand.randint(100,1000)
    list1.append(i)
print(list1)
a=choice(list1)
print()
print(f"Tanlangan son: {a}")
print()
for i in range(a):
    if i%2==0:
        list2.append(i)
print(list2)

#%%
import random as rand
from random import choice
lst=list()
for i in range(1000):
    i=rand.randint(1,1000000)
    lst.append(i)
print(lst)
a=choice(lst)
print()
print(f"Tanlangan son: {a}")
print()
for num in range(a,1000000):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           lst.append(num)
           print(num,end=" ")
