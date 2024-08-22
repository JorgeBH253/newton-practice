import numpy as np 

def optimize(x_0,f):
    def der_1(f,x):
        h = 0.001
        return (f(x+h) - f(x))/h
    
    def der_2(f,x):
        h = 0.001
        return (f(x+h) -2*f(x) +f(x-h) )/h**2
    
    error = 0.00001
    x_t = x_0
    y_t = x_t - der_1(f,x_t)/der_2(f,x_t)
    while np.abs(x_t - y_t) > error:
        x_t = y_t
        y_t =  x_t - der_1(f,x_t)/der_2(f,x_t)
    return y_t