""" 
everything in python is an object
syntax

class Person(Identifier):
    pass (when you dont pass anything)

 """

class Person:
    pass

p = Person()
print(p)

# where person object is present and inside with module)

# methods

class Student:
    name = "jatin"
    def say_hi(self):
        print('hello',self.name)

a = Student()

print(a.say_hi())


# __init__(self):
        #   pass
        # this is called dunders method or magic function
        #  when a new object is created it is called but it is not a constructor



""" 
there are different types of dunder methods called in different time In life cycle of object
in python.

lets say if we call at time of creating then
1-  __init__(self):

if we call while adding objects then
2-  __add__(self,other)
a.__init__(b)  = a+ b (internally how python works on addition of object)

If we want to call  on delete
3 - __del__self()

if we want to do a string operation on object in python
4- __str__
str(a) = a.__str__


equal operation func
__eq__(self,other)
a== b


 """

#  dunders examples

class Car:
    def __init__(self,model,milage):
        self.model = model
        self.milage = milage
    def __str__(self):
        return " {} {}".format(self.model, self.milage)
    def __repr__(self):
        return " {} ".format(self.model)
    def __eq__(self, other):
        return self.milage == other.milage
    def __add__(self,other):
        return self.milage + other.milage


c1 = Car('a',2)
print(c1)
c2= Car('b',4)
print(c2)

sum = c1+c2
print(sum)

print(c1 == c2)


""" 
to print like cout<<"Siv"<<"gouri" like c++ left shift operator there are also dunders


 """

class OutputStream:
    def __lshift__(self,other):
        print(other, end= '')
        return self
cout = OutputStream()

xyz = cout<<"a"<<"sanidev"<<"siv"
print(xyz)
