#%% 1-misol
lst=[1,2,33,5,6,7,7]
n=int(input("n="))
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==n:
            print(i,j)

#%% 2-misol
text = input("matn:")
list_ = list(text)
list_ = text.split()
list_.sort(reverse=False)
print(*list_)

#%% 3-misol
n = int(input("n="))
sum=0
for i in range(1, n + 1):
    sum += i
print(sum)

#%% 4-misol
text=input("text:")
text1=str()
for i in text.split():
    if len(i)%2!=0:
        text1+=i[::-1]
        text+=" "
    else:
        text+=i+" "
text=str(text1)
print(text)

#%% 5-misol
n=int(input("n="))
list_0=list()
while n>0:
    k=n%10
    list_0.append(k)
    n//=2
list_0.reverse()
print(*list_0)
print(list_0.count(0))

#%% 6-misol
n=int(input("n="))
for i in range(n,n+22):
    k=0
    for j in range(2,i//2):
        if i%j==0:
            k+=1
    if k==0:
        print(i,end=" ")

#%% 7-misol
soz=input("soz=")
harf=input("harf=")
for i in range(0,len(soz)):
    if soz[i]==harf:
        print(soz[i].upper(),end="")
    else:
        print(soz[i],end="")

#%% 8-misol
n=int(input("n="))
s=0
for i in range(1,n):
    print("2"*i,end=" + ")
    s+=int("2"*i)
s+=int("2"*n)
print("2"*n,"=",s)
