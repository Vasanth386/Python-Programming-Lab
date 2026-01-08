def fun(base,exp):
    if(exp<0):
        print("invalid")
    elif(exp == 0):
        res=1
    else :
        res=base**exp
    print(res)
base = int(input("enter base number:"))
exp = int(input("enter the power to be raised:"))
fun(base,exp)