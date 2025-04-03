import one 
one.add(2,4)
one.mul(3,4)

#OOPS in python
#OBJECT ORIENTED PROGRAMMING SYSTEM
# OOPS is the methodology and technique to develop real thinking implementation of programming
# why use opps 
# it provide secure programmming, it providees structure 
# it provides reference base
# it provide performance based programming
# it reduced code redundancy and complexity
# components of oops
# class
# object
# method
# attribute
# class is a blueprint or prototype of an object
# method are usefull to perform the logic in a class 
# attributes are usefull to implement logic in a class 
# object is a real life entity of your class 
# features of oops
# polymorphism
# inheritance
# encapsulation
# abstraction
# polymorphism one word to different work is called polymorphism
# we have two types of polymorphism
        # compile time polymorphism (static polymorphism) method overloading
        # run time polymorphism (dynamic polymorphism)  and method overriding
        # we have teo different class having same name method is called method overloading
        # child class method will overiride parent class method is called method overriding
class one:
    def show(self):
        print("this is show method")

class two(one):
    def show(self):
        print("this is show method of class two")

obj = two()
obj.show()

class apple13:
    color = "red"
    camera = "12mp"
    battery = "4000mah"
    def show(self):
        print("color is ",self.color)
        print("camera is ",self.camera)
        print("battery is ",self.battery)

class apple14(apple13):
    # color = "black"
    # camera = "16mp"
    battery = "5000mah"
    def show(self):
        print("color is ",self.color)
        print("camera is ",self.camera)
        print("battery is ",self.battery)

obj = apple14()
obj.show()

# this is method overiding with inheritance

# method overloading
# we have one class more than one same name method with the different signatureis called method overloading
# python does not support method overloading since python is a dynamic language

#inheritance are usefull to share your code
# this is useful to reduce your code complexity
# increase the performance of your code
# resusability of your code
# we have 5 types of inheritance
#   single level inheritance
#   multilevel inheritance
#   mulitple inheritance = single child multiple parent
#   heirarichal inheritance
#   hybrid inheritance


# this is single level inheritance
class A:
    c=10
    d=89
    def add(self):
        z=self.c+self.d
        print(z)
class B(A):
    def mul(self):
        z=self.c*self.d
        print(z)
k=B()
k.add()
k.mul()

# this is multi level inheritance
class C(B):
    def div(self):
        z=self.c/self.d
        print(z)

S=C()
S.div()


# this is the eg of multiple inheritance
class D:
    def mod(self):
        c=15
        d=20
        z=self.c%self.d
        print(z)

class E(A,D):
    def rem(self):
        print("this is rem")
        #even in case of no c and d in class D it will take the values from the other class no matter what is the order

third=E()
third.add()
third.mod()

class F(A,D):
    def rem(self):
        print("this is rem")
        #this will only include the vaules of first class given as para

fourth=F()
fourth.add()
fourth.mod()

