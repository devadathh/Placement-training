l=input().split()
k=int(input())
m=0
for i in range(len(l)-k):
    sum=0
    for j in range(i,i+k):
        sum+=l[j]
    m=max(m,sum)
print(m)