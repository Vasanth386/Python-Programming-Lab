n=input("enter a word:")
m=input("enter a letter:")
l=0
c=0
n+="\0"
if(len(m)>1):
    print("only a letter can be checked")
else:

    while(n[l]!="\0"):
        if(n[l]==m):
            c+=1
        l+=1
    print("no.of times",m,"occurs in",n,":",c)
