string="helloworld"
print(string[4])
print(string[-3])
try:
    print(string[14]) # index out of range
except IndexError:
    print("it is custom index out of range error")
try:    
    string[2]='k'
except TypeError:
    print("item assignment wont support")

print(type(string))
print(dir(string))
help(str)

nums=123333333
print(nums[3])
