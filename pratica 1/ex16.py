import math

Vreal=math.pi**2
eps=1e-5



def res(eps,Vreal):
    i=1
    soma=6/i**2
    i+=1
    while(abs(Vreal-(soma))>=eps):
        soma+=6/i**2
        i+=1

    print(f"Valor aprox: {soma}\nTermos: {i-1}")
    print(f"Erro aprox: {Vreal-soma}")

res(eps,Vreal)