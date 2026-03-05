student = {"id": 101,"name": "Rahul","age": 20}
print("Original Dictionary:", student)
key = input("Enter new key: ")
value = input("Enter value: ")
student[key] = value
print("Dictionary after adding:", student)
u_key = input("Enter the key to update: ")
u_value = input("Enter new value: ")
student[u_key] = u_value
print("Dictionary after updating:", student)