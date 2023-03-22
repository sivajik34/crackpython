x=[20,50,80]
print("list x:",x)

print('copy list x to list y using copy method')
y=x.copy() # shallow copy

print("list y:",y)

print("now pop element from list y ; but it wont effect list x")

print("poped element:",y.pop())

print("list x still contans poped element:",x)
print("list y:",y)

print("now add one more element 45 to x and y wont effect")

x.append(45)

print("list x:",x)
print("list y:",y)


print("copy method in multi dimension elements; if you change copied list it will effect in source list as well")

p=[20,[50,60],80]

print("list p:",p)

print("copy using copy (swallow) method from p to q")
q=p.copy()

print("list q:",q)

print("change 50 to 980 in list q")
q[1][0]=980

print("list p:",p)
print("list q:",q)

print("add element in normal index for list q,it will work,i mean list p wont effect if you change list q vice versa")
q.append(56)
print("list p:",p)
print("list q:",q)
