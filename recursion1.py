def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
n=5
fun(n)