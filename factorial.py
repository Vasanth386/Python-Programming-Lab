#recursion
n=int(input("enter a number:"))
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(n))
#without recursion
n=int(input("enter a number:"))
def fact(n):
    a=1
    if(n==0 or n==1):
        print(a)
    else:
        for i in range(1,n+1):
            a=a*i
        print(a)
fact(n)