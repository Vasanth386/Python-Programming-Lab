#recursion
def prime(n,i=2):
    if(n<=1):
       return None
    elif(2*i>n):
        return True
    elif(n%i==0):
        return False
    return prime(n,i+1)
n=int(input("enter any number:"))
n=abs(n)
print(prime(n))
#non-recursion
n = int(input("enter any whole number:"))
n=abs(n)
def prime(n):
    is_prime=True
    if(n==0 or n==1):
        print("none")
    else:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                is_prime=False
        return is_prime
print(prime(n))
