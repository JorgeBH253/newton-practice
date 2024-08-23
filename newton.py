import numpy as np


def der_1(f,x):
    """
    Takes: a function f and real value x, 
    Returns: an approximation of the derivative of f at that point 
    """
    h = 1e-5
    return (f(x+h) - f(x))/h

def der_2(f,x):
    """
    Takes: a function f and real value x, 
    Returns: an approximation of the second derivative of f at that point 
    """
    h = 1e-5
    return (f(x+h) -2*f(x) +f(x-h) )/h**2
    

def optimize(x_0,f):
    """
    Input:
    - x_0 : initialization point 
    - A function we want to optimize 
    returns:
    - an approximate minimizer. 
    """

    if not isinstance(x_0, (int, float, np.float64)):
        raise TypeError
                       
    if not callable(f):
        raise TypeError(f"Argument is not a function, it is of type {type(f)}")
    if x_0 > 1e7:
        raise RuntimeError
    
    import warnings
    if x_0 > 3:
       warnings.warn(f"{x_0} is greater than 3.")
        
    
    error = 0.00001
    x = x_0
    if np.abs(der_2(f,x))<error: 
        raise TypeError("second derivative is 0 ")
    y = x - der_1(f,x)/der_2(f,x)
    while np.abs(x - y) > error:
        x = y
        if np.abs(der_2(f,x))<error: 
            raise TypeError("second derivative is 0 ")
        y =  x - der_1(f,x)/der_2(f,x)
    return y


