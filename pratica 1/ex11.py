


x=0.5
eps=1e-9

def calcular(x,eps):
    i=0
    termo=1
    soma=0
    while(abs(termo)>=eps):
        soma+=termo
        termo*=(-1)*((x**2)/(i+1))
        i+=1

    print(f"Soma: {soma}\nTermos: {i}")

calcular(0.5,1e-9)
