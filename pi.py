#importing math and decimal functions
from math import factorial
from decimal import Decimal, getcontext
#asking how many digits of pi are wanted (will be stored as Decimal)
getcontext().prec= int(input("how many digits of pi do you want ? "))
#setting veriables
def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    #the calculation
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)                                   
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    #returning the result of the calculation
    return pi
#printing the value
print (calc(25))