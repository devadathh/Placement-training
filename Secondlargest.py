l=list(map(int,input().split()))
max=0
smax=0
for i in l:
    if i>max:
        smax=max
        max=i
    elif i<max and i>smax:
        smax=i
print(smax)