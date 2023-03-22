student=["siva","raghu","rahul"]
marks1=[20,30,40,50]
marks2=[100,200,300]
print("student:",student)
print("marks1:",marks1)
print("marks2:",marks2)
zip_obj=zip(student,marks1,marks2)
print(zip_obj)

print(list(zip_obj))
print(tuple(zip_obj))
