n=int(input())
s=0
count=0
while n>0:
    n=n//10
    count+=1
while n>0:
    r=n%10
    s=s+r**count
    n=n//10
if s==n:
    print("Armstrong")
else:
    print("Not Armstrong")


