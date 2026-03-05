n = int(input("Enter number of tuples: "))
t_list = []
for i in range(n):
    a = int(input("Enter first element: "))
    b = int(input("Enter second element: "))
    t_list.append((a, b))
t_list.sort(key=lambda x: x[-1])
print("Sorted list of tuples:", t_list)