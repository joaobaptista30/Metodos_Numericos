import math
math.sqrt

eps=1e-4
x=1.1



def res(x,eps):
    i=1
    termo=1.1 #termo inicial
    soma=termo
    i+=1
    termo*=-1 * (x**2)/((2*i+1)*(2*i))
    while(math.sqrt(1-soma**2)>=eps):
        soma+=termo
        i+=1
        termo*=-1 * (x**2)/((2*i+1)*(2*i))

    print(f"Soma: {math.sqrt(1-soma**2)}\nTermos: {i-1}")


res(x,eps)