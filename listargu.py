def count(lst):
    c1=0
    c2=0
    for i in lst:
        if(i%2==0):
            c1+=1
        else:
            c2+=1
    print("no.of even:",c1)
    print("no.of odd:",c2)
n=int(input("enter size of list:"))
l=[]
for i in range(n):
    v=int(input(f"enter element {i} : "))
    l.append(v)
count(l)