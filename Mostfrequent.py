l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
ele1,ele2,max,smax=0,0,0,0
for i in d:
    if d[i]>max:
        smax=max
        ele2=ele1
        ele1=i
        max=d[i]
    elif d[i]<max and d[i]>smax:
        smax=d[i]
        ele2=i
print(ele1,ele2)