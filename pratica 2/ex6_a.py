import math



a=2
b=6
eps=1e-1

def f(x):
    return 2*math.log(x)-x+2

def f1_derivada(x):
    return 2/x -1

def f2_derivada(x):
    return -2/x**2

def f_newton(x):
    return x-(f(x)/f1_derivada(x))

def resolucao_alinea_A(error,min,max):
    
    f_min=f(min)

    while(abs(min-max)>error):
        m=(min+max)/2
        f_m=f(m)
        if(f_m==0):
            print(f'{m} é a raiz exata')
            return m
        elif(f_m*f_min>0):
            min=m
        elif(f_m*f_min<0):
            max=m

    print(f'intervalo é [{min},{max}]')

resolucao_alinea_A(eps,a,b)

a,b=5.3,5.4
m=f2_derivada(b)/(2*f1_derivada(b))
print(m)

def metodo_newton(a,b,m):

    erro_max=abs(a-b)
    i=1
    x0=f_newton(b)
    while i<=3:
        x1=f_newton(x0)
        x0=x1
        erro_max= m * erro_max**2
        print(f'iteracao: {i} | x1: {x1} | Majorante: {erro_max}')
        i+=1
        
    


        
metodo_newton(a,b,m)