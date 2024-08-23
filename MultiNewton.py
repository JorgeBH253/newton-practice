import autograd.numpy as np
from autograd import grad, hessian 

def M_Newton(x_0,f,tol=1e-7): 
    nabla_f, H_f, x = grad(f), hessian(f), x_0
    nabla_f_x, H_f_x = nabla_f(x), H_f(x)
    #check if hessian is invertible: 
    if np.linalg.det(H_f_x) == 0: 
        raise TypeError('Hessian not invertible')
    inv_Hfx = np.linalg.inv(H_f_x)
    x_new =  x - inv_Hfx@ nabla_f_x
    while np.linalg.norm(x-x_new) > tol:
        x = x_new 
        nabla_f_x, H_f_x = nabla_f(x), H_f(x)
        x_new = x - inv_Hfx@ nabla_f_x
        print(x_new)
    return x_new 

    