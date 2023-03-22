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

# clear function example
sample_list=[2,5,7,'green',True,8.5]
print(type(sample_list))
print(sample_list)
print("clear function")
sample_list.clear()
print(sample_list) #it will print []

# + in list
p=[20,30,40,50]
q=[35,78,90,20,45,20]
print("list p:",p)
print("list q:",q)
r=p+q
print("p+q:",r)
print("20 element count:", r.count(20))

r.extend([90,110,555])

print("after extend list r:",r)

r.reverse()

print("list after reverse",r)

r.remove(20) # it will delete first matching element even 20 number presented multiple times
print("after remove 20 element",r)

print("110 element index:",r.index(110))

r.insert(2,"yellow")

print("after insert:",r)
