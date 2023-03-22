my_list=[]
print(type(my_list))
#<class 'list'>

list1=list() # built in mutable sequence
print(type(list1))
#<class 'list'>
print(id(list1))
#140589007633152  # memory address sample
print(dir(list1))
print(help(list1))

my_list=list('xyz') #string is iterable sequence, so it will print ['x','y','z']
print(my_list)

list1.append(20)
list1.append(30)
# list1[2]=40  IndexError: list assignment index out of range
list1.append(40)
list1.append(50) 

print(list1)  #[20,30,40,50]

print("copy using equal operator list2=list1")
list2=list1  # list1 and list2 both reference to same object, so if you change list1 or list2 then it will effect both.

print(list2) #[20,30,40,50]
print(id(list2)) #it will print same id of list1


list2[1]=500 # it will change list1 as well

print(list2)
print(list1)

list1[2]=600 #it will change list2 as well

print(list1)
print(list2)

# clear function example
sample_list=[2,5,7,'green',True,8.5]
print(type(sample_list))
print(sample_list)
sample_list.clear()
print(sample_list) #it will print []

print("sorting list1, It will change list2 as well")
print(list1.sort()) #it will return None
print(list2)
print(list1)

