student = {"id": 101,"name": "Rahul","age": 20,"course": "CSE"}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
student.pop("age")
print("After pop():", student)
del student["course"]
print("After delete:", student)