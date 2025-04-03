#  Exception handling :-  It is run time error
'''
Exception handling is of two type :-
1:- Run time error :- it is also called dynamic error
2:- Compile time error :-it is also called static error

--> Error  interrupt the code

We have 4 ways of code to handle exception:-
1:- try
2:- except 
3:- raise
4:- finally
'''

# try and except
# try:
#     x=10
#     y=0
#     z=x/y
#     print(z)
# except Exception as e:
#     print(e)

# print("hello")

# Raise :- Raise are useful to through user define exception

def divide(x,y):
    if(y==2):
        raise Exception("you can divide by 2")
    else:
        z=x/y
        print(z)
try:
    divide(10,2)
except Exception as e:
    print(e)
# print("hello")

# finally :- It is useful to print compalsary  statements if exception is occur or not
'''
try:
    x=10
    y=0
    z=x/y
    print(z)
finally :
    print("hello")'''

# Regular expression :- regular expression is a  pre-define pattern programming.