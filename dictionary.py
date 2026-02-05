student = {
    "name":"tulsi",
    "age" :20,
    "location":"banglore"
}
'''print(student.values())
student.pop("name")
print(student)
print(student.popitem())
student.update({"age":30})
print(student)'''
print(student.get("location"))
print(student["name"])