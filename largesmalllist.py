n=int(input("enter size of list:"))
l=[]
for i in range(n):
    v=int(input(f"enter element {i} : "))
    l.append(v)
max=l[0]
min=l[0]
for i in range(n):
    if(l[i]<min):
        min=l[i]
    if(l[i]>max):
        max=l[i]
print("maximum element in list is:",max)
print("minimum element in list is:",min)
