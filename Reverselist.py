l=input().split()
l1=len(l)
temp=0
c=-1
for i in range(0,l1//2):
    temp=l[i]
    l[i]=l[c]
    l[c]=temp
    c-=1
print(l)