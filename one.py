# parameterized funct
def add(x,y,z):
    t=x+y+z
    print(t)
add(5,4,4)

def mul(a,b):
    c=a*b
    print(c)

# default or parameter less function
def add():
    x=10
    y=90
    print(x+y)

# default parameterized function
# anonymous function is a inline function it is defined by lambda keyword it stores output on a variable
    #short terminologies
    #single expression can be performed only
    #we cant perform conditional statements in it except single if else

p=lambda x,y:x+y
print(p(4,5))
print(p(4,5)-12) #this subtraction can be done in anony funct as it stores output as a variable

s=lambda x,y:x*y/100
print(s(30000,5))

k=[100,200,300] #this will not be passed inside anony funct due to list

# map()
# filter()
# reduce()
# these are extra ordinary function and will be used in anony funct to iterate over a list
# now we use map function 
l=[2,3,4]
z=[3] 
t=list(map(lambda x,y:x*y/100,k,z))
print(t)


a1=[10000,20000,30000,40000,50000,60000]
r1=list(map(lambda x:x>20000 and x<60000,a1))
r2=list(filter(lambda x:x>20000 and x<60000,a1))
print(r1)
print(r2)

#reduce in anony
import functools
ak=['hello','how','are','you']
re=functools.reduce(lambda x,y:x+' '+y,ak)
print(re)
# print(type(re))

li=[1,2,3,4,5,6,7,8,9,10]
re=functools.reduce(lambda x,y:x+y,li)
print(re)

#return type function
def add(x,y):
    return x+y
print(add(4,5))

#multiple value return function
def cal(x,y):
    return x+y,x-y,x*y
print(cal(4,5))

m=['hello','how','are','you']
def calc(m):
    m.remove('how')
    return m
print(calc(m))

#recursive function
#it is a process in which a function calls itself again and again until a condition is met to return a result
#factorial of a number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fibonacci series using recursive function not the sum of the series
def fib(n):
    if n==1:
        return 1
    elif n<=0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
print("fibo series")
print(fib(5))

#argument parameterized function
# these are used to create dynamic argument functions
def show(*args):
    print(args)
show(1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')
#only one *args can be used in a function and it will be the last parameter in the function
def show(a,*args):
    print(a)
    print(args)
show('akshat',1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')    

#keyword argument parameterized function
def shows(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
shows('akshat',1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e',x=1,y=2,z=3)
#this return the output in the form of dictionary by using keyword argument parameterized function

#iterable function

g=2341
# lq=[]
# while g>0:
#     lq.append(g%10)
#     g=g//10
# print(lq) 
#bad approach
gi=str(g)
for i in gi:
    print(i)
#good approach

su=0
for i in gi:
    su+=int(i)
print(su)

#generator function
#it is used to create an iterator
#yield keyword is used to create a generator function
#return keyword is replaced by yield keyword to throw the multiple outputs of the function without ending the function
def she():
    for i in gi:
        yield i
print(list(she()))

#decorator
#it is a user defined function 
# these are usefull to apply existing functionallity to a function without changing the code or the original function 
# they cant be called directly
#these are denoted by @ symbol
# they also have a function inside a function 

#ebill(100,10) #this is the original function

#making decorator fuction
def dec(ebill):
    def wrapper(u,r):   #u,r are the parameters of the original function ebill
        if u<0 or r<0:
            print('invalid')
        else:
            return ebill(u,r)
    return wrapper      #we have to return the wrapper function to the decorator function surely

@dec
def ebill(u,r):
    total=u*r
    print(total)
ebill(100,10) #this is the decorator function
# the sequence of the decorator function is important and cant be changed as it will not work as it is interpretor by function