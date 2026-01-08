#2D Array
arr1 = [(2,3,6),(8,5,2,),(8,7,4)]
arr2 = [(8,5,8),(6,3,7),(4,8,4)]
import numpy as num
print(arr1+arr2)
numarr1 = num.array(arr1)
numarr2 = num.array(arr2)
print(numarr1+numarr2)
print(numarr1*numarr2)
print(numarr1/numarr2)
print(numarr1-numarr2)
r=numarr1+numarr2
print(r[0,0])
print(r[0:2,2])
