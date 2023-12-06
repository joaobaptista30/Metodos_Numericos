import math

a=1.20
b=1.21
eps=1e-7

def f(x):
    return math.e**(math.sin(x)/5)


def res_met_iter(x0,error):
    x1=f(x0)
    n=1
    while abs(x1-x0)>error:
        x0=x1
        x1=f(x0)
        n+=1
    
    print(f'Valor aprox: {x1:.7f}\nNum de iter: {n}')


res_met_iter(a,eps)