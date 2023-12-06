
def next_termo(i):
    return (i**2)/((i**4)+1)


eps=5*10**-5
i=1
termo=next_termo(i)
soma=termo
i+=1
def metodo_impirico(eps,termo,i,soma):
    while(abs(next_termo(i)-termo)>=eps):
        termo=next_termo(i)
        soma+=termo
        i+=1

    print(f"Soma: {soma}\nTermos: {i-1}")

metodo_impirico(eps,termo,i,soma)