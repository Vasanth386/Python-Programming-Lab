#recursion
n=int(input("enter no.of terms:"))
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fib(n-1)+fib(n-2))
for i in range(n):
    print(fib(i),end=" ")
#iteration
n=int(input("enter no.of rows:"))
def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        for i in range(n):
            print(a,end=" ")
            c=a+b
            a=b
            b=c
fib(n)