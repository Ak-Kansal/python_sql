# 50000 gives 10
# 30000 gives 5
# 20000 gives 2
# below this no discount

def change(total):
    def discount(d):
        if d>50000:
            print("your total amount is: ",d)
            return total(d-(d*10)/100) 
        elif d>30000 and d<50000:
            print("your total amount is: ",d)
            return total(d-(d*5)/100)
        elif d>20000 and d<30000:
            print("your total amount is: ",d)
            return total(d-(d*2)/100)
        else:
            print("your total amount is: ",d)
            return d
    return discount

        
@change
def total(s):
    return s

j=total(5000)
print("your discounted value is:",j)

