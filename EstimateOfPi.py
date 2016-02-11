"""
program:srinivasan ramanujam estimate of pi
created: 11th Feb 2016
author: anoop vasant kumar

"""
import math
def factorial(n):
    if not isinstance(n, int): return -1
    
    if n == 0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)
        
def estimate_pi():
    coef = 2* math.sqrt(2)/9801
    k=0
    sum = 0.0
    term = 0.0
    while True:
        term = (factorial(4*k)*(1103+26390*k)) /(factorial(k)**4 * 396 ** (4*k))
        sum = sum + term
        if term < 1e-15:
            break
        k = k + 1
    print (1.0/math.pi)**-1
    print (coef*sum)**-1

estimate_pi()
