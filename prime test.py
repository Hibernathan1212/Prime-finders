import time
import math

def pi(iterations = 64): #Francois Viete
    a = 0
    sum = 1
    for i in range(iterations):
        a = sqrt(2 + a)
        sum *= (a/2)
    pi = (1/sum) * 2
    return pi

def pow(x, power, modulo = 1): #works only for positive powers + slow
    result2 = 1
    result = 1
    while (power >= 1):        
        result *= x
        power -= 1
    return result

def sqrt(x): #works
    aprx = 8
    for i in range(64):
        aprx = (aprx+x/aprx)/2
        if aprx*aprx == x:
            break
    return aprx 

def prime(n):
    result = fac(n-1)
        #print(i + result)
    result += 1
    result /= n
    print(result)
    print(round(result,2))
    return round(result,2)

pi = pi()

def fac(n):
    a = sqrt(2*pi*n)
    b = pow((n/math.e), n)
    print(sqrt(2*pi*n)*pow((n/math.e), n))
    return round(sqrt(2*pi*n)*pow((n/math.e), n),0)



start = time.time()
n = 2**3169
if (round(prime(n),1).is_integer()):
    print("true")
else:
    print("false")

end = time.time()
#print(end-start)