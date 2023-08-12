class MyStudent:
     name="Sivakumar"
     marks=100
     def __lt__(self,other):
         print("now its implemented")

student=MyStudent()
setattr(student,"name","rao")
setattr(student,"marks",70)
setattr(student,"age",80)
print(student.name,student.marks,student.age)

s2=MyStudent()
setattr(s2,"name","vindor")
setattr(s2,"marks",90)
setattr(s2,"age",90)

print(student.__lt__(s2))
print(student.__gt__(s2)) #NOT IMPLEMENTED
print(student<s2)
print(student>s2)

print(MyStudent.__mro__) #method resoultion order
print(MyStudent.__class__)
print(student.__class__)
delattr(MyStudent,"name")
delattr(student,"name")
#print(student.name)
print(getattr(student,"age"))


