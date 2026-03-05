student = {"101": "Rahul","102": "Anita","103": "Kiran","104": "Sneha"}
value = input("Enter the value to search: ")
for key,val in student.items():
    if val == value:
        print("Key for the given value is:", key)
        break
else:
    print("Value not found in dictionary")