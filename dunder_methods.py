class AddExample:
    def __init__(self,val):
            self.val=val
    def __add__(self,val2):
            return AddExample(self.val+val2.val)
obj1=AddExample("siva") 
obj2=AddExample("kumar")
obj3=obj1+obj2
print(obj3.val)
