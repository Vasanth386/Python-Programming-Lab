
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))
a = p * (1+r/100)**t
ci = a-p
print("compound Interest =",ci)