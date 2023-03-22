list1=[20,50,80]
print('list1:')
print(list1)

print('copy list1 to list2 using copy method')
list2=list1.copy() # shallow copy

print("now pop element from list2 ; it wont effect list1")

print(list2.pop())

print('list2:')
print(list2)
print('list1:')
print(list1)

print("add one more element to list1 and list2 wont effect")

list1.append(45)


print("list1",list1)
print("list2",list2)


print("copy method in multi dimension elements; if you change copied list it will effect in source list as well")

l1=[20,[50,60],80]

print("l1:",l1)

l2=l1.copy()

print("l2:",l2)

l2[1][0]=980

print("l1:",l1)
print("l2:",l2)

print("add element in normal index for l2,it will work,i mean l1 wont effect if you change l2 vice versa")
l2.append(56)
print("l1:",l1)
print("l2:",l2)
