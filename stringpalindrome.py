#method 1
n=input("enter a string:")
l=0
r=len(n)-1
flag=0
while(l<=r):
    if(n[l]==n[r]):
        l+=1
        r-=1
        flag=1
    else:
        break
if(flag==1):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
#method 2
n=input("enter a string:")
m=n[::-1]
if(m==n):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")