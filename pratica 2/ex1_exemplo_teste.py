import math

ext_1=0.1
ext_2=0.2
eps=1e-5

def F(x):
    return math.log(x)-(x**2)+2

#valor aprox logo fazer abs(Xn+1-Xn)


def deriv_F(x):
    return (1/x)-2*x

def deriv_2_F(x):
    return (1/x)-2


def f(x):
    return x-(F(x)/deriv_F(x))




def metodo_Newton(x0,error):
    x1=f(x0)
    n=1
    while abs(x1-x0)>error:
        x0=x1
        x1=f(x0)
        n+=1
    print(f'Num de iter: {n}\nx0: {x1:.9f}\n')





metodo_Newton(0.1,eps)
