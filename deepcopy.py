print("import copy module, it is required for deepcopy purpose")
import copy

x=[90,[75.45,True,90],80,67]
print("list x:",x)

print("copy list x to list y using deepcopy")
y=copy.deepcopy(x)

print("now change element in list y")
y[1][1]=False
print("list x remains same")
print("list x:",x) 
print("list y:",y)

