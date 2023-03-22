def func1(val):
    return val*val
result=map(func1,range(1,21))
print(list(result))

x=[4,5,6]
y=[7,8,9]
print("x:",x)
print("y:",y)
result=map(lambda x,y: x+y,x,y)
print(list(result))
