x=[20,30,40,50]
print('list x:',x)  #[20,30,40,50]
print('list x memory address:',id(x)) 
print("")
print("copy using equal operator y=x")
y=x  # list x and list y both reference to same object, so if you change list x or list y then it will effect both.


print('list y:',y) #[20,30,40,50]
print('list y memory address same as list x:',id(y)) #it will print same id of list x

print("")
print("change list y element from 30 to 500")
y[1]=500 # it will change list x as well

print('list x:',x)
print('list y:',y)

print("")
print("change list x element from 40 to 600")
x[2]=600 #it will change list y as well

print('list x:',x)
print('list y:',y)

print("")
print("sorting list x, It will change list y as well")
print("return value of sorting:",x.sort()) #it will return None
print('list x:',x)
print('list y:',y)


