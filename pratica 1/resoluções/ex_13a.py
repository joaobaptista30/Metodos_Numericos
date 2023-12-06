

def calc_termo(k):
    return (-1)**k*k/(5**k+10)

def aprox_serie_alternada(erro):
    soma = 0
    i = 1
    while not (abs(calc_termo(i)) < erro):
        soma += calc_termo(i)
        i += 1
    print(f"Resultado: {soma}\nUltimo termo adicionado: {i-1}")


erro=5*10**-4

aprox_serie_alternada(erro)