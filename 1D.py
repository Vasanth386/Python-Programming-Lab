#array 
list = [86,11,23,90,45,36,83,42,19,100,56]
print(list)
print(type(list))
import numpy as nm
nmlist = nm.array(list)
print(nmlist)
print(nm.max(nmlist))
print(nm.min(nmlist))
print(nm.mean(nmlist))
print(nm.std(nmlist))
print(nm.var(nmlist))
print(nm.where(nmlist>=50,"GOOD","DECENT"))
print(nm.where(nm.mean(list) >= 50 , "GOOD","DECENT"))
print(nm.where(nm.mean(list) < 30 , "POOR","DECENT"))
print(type(nmlist))
#1D array operations
arr1 = [2,5,1,3]
arr2 = [4,2,8,3]
print(arr1+arr2)
import numpy as np
nparr1 = np.array(arr1)
nparr2 = np.array(arr2)
print(nparr1+nparr2)
print(nparr1*nparr2)
print(nparr1%nparr2)
print(list[0])
print(list[0:5])
print(list[3:6])



