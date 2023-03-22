class Class1:
      def m(self):
          print("from class1")
class Class2(Class1):
      def m(self):
          print("from class2")
class Class3(Class1):
      def m(self):
          print("from class3")
class Class4(Class2,Class3):
      pass
      
      
obj=Class4()
obj.m()  

class Class5:
      def m(self):
          print("from class5")
class Class6(Class5):
      def m(self):
          print("from class6")
class Class7(Class5):
      def m(self):
          print("from class7")
class Class8(Class7,Class6):
      pass
      
      
obj=Class8()
obj.m()                                                                      
