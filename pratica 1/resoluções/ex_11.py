

def calc_termo(n,x):

    fatorial_n=1    
    i=1
    while (i<=n):
        fatorial_n*=i
        i+=1

    return (-1)**n*x**(2*n)/fatorial_n
    

def aprox_serie_alternada(erro):
    soma = 0
    x=0.5
    i = 0
    while not (abs(calc_termo(i,x)) < erro):
        soma += calc_termo(i)
        i += 1
    print(f"Resultado: {soma}\nUltimo termo adicionado: {i-1}")


aprox_serie_alternada(1e-9)

