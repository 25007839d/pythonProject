# class Father():
#     def __init__(self):
#         super().__init__()
#         self.model="Realme X"
#
# class Mother():
#     def __init__(self):
#         super().__init__()
#         self.model1=100
#
#
# class Son(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         self.model2="nice"
#
#     # def show2(self):
#
#         print("Model:",self.model,"price:",self.model1,"feature:",self.model2)
# ob=Son()
#
# print(issubclass(Son, Father))
import collections

# word count ----------------------------------------
# word_count=0
# with open(r'C:\Users\Dell\Desktop\rdd.txt','r') as file:
#     for line in file:
#         word_count += len(line.split(','))
#
# print("number of words : ", word_count)
#----class & instance variable

# class Car:
#     model= 'classic'
#
#
#     def __init__(self):
#         self.price=100000
#
#
#     @classmethod
#     def show(cls):
#         print(cls.model)
# ob=Car()
# print(ob.model,ob.price)
#
# ob1=Car()
# print(ob1.model,ob1.price)
#
# # ob.model='top'
#
# Car.model='gdg'
# ob.price=20000
#
# print(ob.model,ob.price)
#
# print(ob1.model,ob1.price)

#  inner calass------------------------

# class Student:
#
#     def __init__(self):
#         self.name='rahul'
#         self.rono='10'
#         self.lap=self.Laptop()
#
#     def show(self):
#         print(self.name,self.rono)
#         self.lap.show()
#
#     class Laptop:
#         def __init__(self):
#             self.brand='hp'
#             self.modle='latirude'
#         def show(self):
#             print(self.brand,self.modle)
#
# ob =  Student()
# ob.show()

# ob.Laptop().show()
# poly morphisim----------methodoverloading-----a function can be called with diffrent number of arguments

class Mover():
    def show(self,a=None,b=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None:
            print(a)
        elif b!=None:
            print(b)
# ob = Mover()
# ob.show(10,20)
# ob.show(10)


#   method-overriding-multiple function with same number and same number of parameter

class Father:
    def show (self):
        print (" This is a father class")

class Son(Father):
    def show (self):
        print("This is a son class")  # method overriding

# ob = Son()
# ob.show()

#-------------when we need both meyhod..............use supper function-------------------

class Father:
    def show (self):
        super().show()
        print (" This is a father class")

class Mother:
    def show (self):

        print("This is a Mother class")

class Son(Father,Mother):  #  use MRO (method resolution order) left to right
    def show (self):
        super().show()

        print("This is a son class")  # method overriding

# ob = Son()
# ob.show()


#----operator overloading------------------------

class Opload:
    def ret(self,a,b):
        self.c=a+b
        return self.c
    def __add__(self, other):  # operator overloqading with magic method
        return self.c+other.c

ob=Opload()
ob.ret(2,2)

ob1=Opload()
ob1.ret(2,1)

s = ob+ob1
# print(s)

# Duck typing -------it dosent matter which class it is ,matter is method should be same-------

class Duck():
    def dush(self):
        print(" hi it is a 1st duck method")

class Cat():
    def dush (self):
        print("cat cat -----------------+"
              "*******************")
class Dog():
    def dush(self):
        print(" bho bhoi ***********---------%%%%%^&&&&&&&*&^&&&&&&")


dk= Dog()
dk.dush()

dk=Cat()
dk.dush()

dk=Duck()
dk.dush()

