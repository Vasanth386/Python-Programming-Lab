n=int(input("enter a number of elements:"))
c1 = 0
c2 = 0
for i in range(1,n+1):
    if(i%2 == 0):
        c1 = c1+1
    else:
        c2 = c2+1
print(c1)
print(c2)
