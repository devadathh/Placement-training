n=int(input())
s=0
count=0
rev=0
t=n
while t>0:
    t=t//10
    count+=1
t=n
while t>0:
    ld=t%10
    rev=rev*10+ld
    t=t//10

while rev>0:
    r=rev%10
    s=s+r**count
    rev=rev//10
    count-=1
print(s)
