n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
n3 = int(input("enter third number:"))
max=0
min=0
if(n1<n2):
    if(n1<n3):
        min = n1
    else:
        min = n3
else:
    if(n2<n3):
        min = n2
    else:
        min = n3
print(min)
if(n1>n2):
    if(n1>n3):
        max = n1
    else:
        max = n3
else:
    if(n2>n3):
        max = n2
    else:
        max = n3
print(max)
  