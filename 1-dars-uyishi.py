#%% Begin-22
a=input("a=")
b=input("b=")
c=a
a=b
b=c
print("a =",a)
print("b =",b)

#%% Begin-23
a=input("a=")
b=input("b=")
c=input("c=")
d=a
a=c
c=b
b=d
print("a =",a)
print("b =",b)
print("c =",c)

#%% Begin-24
a=input("a=")
b=input("b=")
c=input("c=")
d=a
a=b
b=c
c=d
print("a =",a)
print("b =",b)
print("c =",c)

#%% Integer-6
a=int(input("a="))
b=int(a/10)
c=int(a-b*10)
print("o'nliklar xonasi: ",b)
print("birliklar xonasi: ",c)
#%% Integer-7
a=int(input("a="))
b=int(a/10)
c=int(a-b*10)
d=b+c
print("raqamlari yig'indisi:",d)

#%% Integer-8
a=int(input("a="))
b=int(a/10)
c=int(a-b*10)
d=b
b=c
c=d 
print("almashgandan so'ng: ",b,c,sep="")

#%% Integer-9
a=int(input("a="))
b=int(a/100)
print(b)

#%% Integer-10
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
print("birliklar xonasi: ",e)
print("o'nliklar xonasi: ",d)

#%% Integer-11
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
f=b+d+e
print("raqamlari yig'indisi: ",f)

#%% Integer-12
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
print("teskarisi:",e,d,b,sep="")

#%% Integer-13
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
f=b+100*d+10*e
print("natija:",f)

#%% Integer-14
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
f=b*10+d+100*e
print("natija:",f)

#%% Integer-15
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
f=b*10+d*100+e
print("natija:",f)

#%% Integer-16
a=int(input("a="))
b=int(a/100)
c=int(a-b*100)
d=int(c/10)
e=int(c-d*10)
f=b*100+d+e*10
print("natija:",f)

#%% Integer-17
a=int(input("a="))
b=int(a/1000) 
c=int(a/100)
d=int(c-b*10)
print("natija:",d)

#%% Integer-18
a=int(input("a="))
b=a/1000
print("natija:",int(b))

#%% Integer-19
a=int(input("a="))
b=a/60
print(int(b),"minut o'tgan")

#%% Integer-20
a=int(input("a="))
b=a/3600
print(int(b),"soat o'tgan")

#%% Integer-21
a=int(input("a="))
b=a/60
c=a-int(b)*60
print(int(b),"minut ",c,"sekund o'tgan")

#%% Integer-22
a=int(input("a="))
b=a/3600
c=a-int(b)*3600
print(int(b),"soat ",c,"sekund o'tgan")

#%% Integer-23
a=int(input("a="))
b=a/3600
c=a-int(b)*3600
d=int(c/60)
e=c-int(d*60)
print(int(b),"soat ",d,"minut ",e,"sekund o'tgan")