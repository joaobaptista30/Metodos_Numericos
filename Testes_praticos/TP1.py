

def termo(n):
    return((n**3)/(2**n))


i=1
soma=0
l=1/2
eps= 5*10**(-4)

while(abs(termo(i)/(1-l))>=eps):
    soma+=termo(i)
    i+=1



print(f"Soma: {soma}\nTermos: {i-1}")

