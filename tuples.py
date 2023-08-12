my_tuple=(25,56,89,[23,45,56])
print(type(my_tuple))
print(id(my_tuple))

print(my_tuple[1])
print(my_tuple[3][0])
my_tuple[3][0]=900
my_tuple[3]=[23,58,67]
print(my_tuple)
my_tuple[1]=78
