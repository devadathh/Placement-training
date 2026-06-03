l=list(map(int,input().split()))
c=0
m=0
for i in l:
    if i>m:
        m=i
        c+=1
print(c)