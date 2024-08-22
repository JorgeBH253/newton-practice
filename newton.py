import numpy as np

def der_1(f,x):
        h = 0.001
        return (f(x+h) - f(x))/h

def der_2(f,x):
        h = 0.001
        return (f(x+h) -2*f(x) +f(x-h) )/h**2
    

def optimize(x_0,f):
    error = 0.00001
    x = x_0
    y = x - der_1(f,x)/der_2(f,x)
    while np.abs(x - y) > error:
        x = y
        y =  x - der_1(f,x)/der_2(f,x)
    return y_t

