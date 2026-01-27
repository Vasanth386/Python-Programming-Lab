n=int(input("enter size of list:"))
l=[]
sum=0
print("enter list elements:")
for i in range(n):
    v=int(input(f"enter element {i} :"))
    l.append(v)
    sum+=l[i]
print("sum is:",sum)
