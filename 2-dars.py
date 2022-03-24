#%% Format function
a=123
b=3.14789
c="Hello"
d=True
print("a={:05} b={:.3f} c={} d={}".format(a,b,c,d))
print("a={0} b={1} c={2} d={3}".format(a,b,c,d))
print(f"a={a} b={b} c={c} d={d}")
print(f"Hello so'zida {len(c)} ta belgi bor")

#%% Taqqoslash amallari
'''
>, <, >=, <=, ==, !=, and, or, not
'''

print("5>3",5>3)
print("5<3",5<3)
print("5>=3",5>=3)
print("5<=3",5<=3)
print("5==3",5==3)
print("5!=3",5!=3)
print("5>3 and 1!=2",5>3 and 1!=2)
print("5<3 or 1!=2",5<3 or 1!=2)
print("not(5>3 and 1!=2)",not(5>3 and 1!=2))

#%% If elif else
a=int(input("sonni kiriting: "))
if a>0:
    print("son musbat")
elif a<0:
    print("son manfiy")
else:
    print("son nolga teng")
    
#%% Ichma-ich if
a=10; b=20; c=30
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>c:
    print(b)
else:
        print(c)
        
#%% While and for
i=1
while i<10:
    print(i)
    i+=1
k=0
while 1:
    while 1:
        k+=1
        if k==4 or k==6:
            continue        
        print("salom",k,end=' ')
        if k==10:
            break
    if k==10:
        break
    
#%% In function
text="Salom bolalar"
if 'a' in text:
    print("a harfi textda bor")
else:
    print("a harfi textda yo'q")

if 'bola' in text:
    print("bola harfi textda bor")
else:
    print("bola harfi textda yo'q")

#%% For
text="Salom"
for i in text:
    print(i,end=" ")
print()
for i in range(1,10):
    print(i,end=" ")
text="Foundation 32"
matn=str()
print()
for i in range(0,len(text)):
    if text[i]=='a':
        matn+='o'
    elif text[i]=='o':
        matn+='a'
    else:
        matn+=text[i]
print(matn)

#%% 1-misol
n=int(input("n="))
for i in range(2,n+1,2):
    print(i,end=" ")
print()

#%% 2-misol
n=int(input("n="))
for i in range(1,n+1,2):
    print(i,end=" ")
print()

#%% 3-misol
n=int(input("n="))
a=0
b=0
for i in range(1,n+1):
    if i%2!=0:
        a+=1
    else:
        b+=1
print(a,"ta toq va",b,"ta juft")

#%% 4-misol
a=int(input("a="))
b=int(input("b="))
if a<b:
    while b%2==0:
        print(b-4,b-2,b)
        if b==b:
            break
    while b%2!=0:
        print(b-5,b-3,b-1)
        if b==b:
            break   
if a>b:
    while a%2==0:
        print(a-4,a-2,a)
        if a==a:
            break
    while a%2!=0:
        print(a-5,a-3,a-1)
        if a==a:
            break

#%% 5-misol
a=int(input("a="))
b=int(input("b="))
if a<b:
    while a%2==0:
        print(a+1,a+3,a+5)
        if a==a:
            break
    while a%2!=0:
        print(a,a+2,a+4)
        if a==a:
            break   
if a>b:
    while b%2==0:
        print(b,b,b)
        if b==b:
            break
    while b%2!=0:
        print(b,b,b)
        if b==b:
            break

#%% 6-misol











 