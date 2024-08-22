import numpy as np

def der_1(f,x):
    """
    Takes: a function f and real value x, 
    Returns: an approximation of the derivative of f at that point 
    """
    h = 0.001
    return (f(x+h) - f(x))/h

def der_2(f,x):
    
    """
    Takes: a function f and real value x, 
    Returns: an approximation of the second derivative of f at that point 
    """
    h = 0.001
    return (f(x+h) -2*f(x) +f(x-h) )/h**2
    

def optimize(x_0,f):
    """
    Input:
    - x_0 : initialization point 
    - A function we want to optimize 
    returns:
    - an approximate minimizer. 
    """
    error = 0.00001
    x = x_0
    y = x - der_1(f,x)/der_2(f,x)
    while np.abs(x - y) > error:
        x = y
        y =  x - der_1(f,x)/der_2(f,x)
    return y

