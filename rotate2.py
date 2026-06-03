l=input().split()
temp=l[0]
for i in range(len(l)-1):
    l[i]=l[i+1]
l[-1]=temp
print(l)